###############################################################################
# Filename: Model.py                                                           #
# Project: TomorrowNow                                                         #
# File Created: Tuesday October 4th 2022                                       #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Mon Nov 07 2022                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2022 TomorrowNow                                               #
#                                                                              #
# TomorrowNow is an open-source geospatial participartory modeling platform    #
# to enable stakeholder engagment in socio-environmental decision-makeing.     #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
#                                                                              #
###############################################################################
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.gis.db.models.aggregates import Union
from django.contrib.gis.db.models.functions import Centroid, AsGeoJSON
from world.models.County import County  # new
from .OPEnums import PrivacyEnum, StatusEnum
from .OPModelGoal import ModelGoal
from .OpenModelExtent import ModelExtent
from savana.utils import actinia as acp
import requests

# class GoalsEnum(models.TextChoices):
#     PROTECT = "PNR", "Protect Natural Reasources"
#     FRAGMENT = "LLF", "Limit Landscape Fragmentation"
#     ROAD_FLOODING = "RFOR", "Reduce Flooding Over Roads"
#     PROPERTY_DAMAGE_FLOODING = "RPDF", "Reduce Property Damage from Flooding"
#     WATER_QUALITY = "WQ", "Protect Water Quality"


class OpenPlainsModel(models.Model):
    """
    A base model that will hold all other models.
    """

    name = models.CharField(max_length=250)  # The model name
    description = models.CharField(max_length=250)  # The model description
    status = models.CharField(max_length=2, choices=(StatusEnum.choices), default=StatusEnum.INITIATING)
    privacy = models.CharField(max_length=2, choices=(PrivacyEnum.choices), default=PrivacyEnum.PRIVATE)
    location = models.CharField(max_length=250, null=True)  # TODO: Switch to Location Model
    mapset = models.CharField(max_length=250)  # TODO: Switch to Mapset Model
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='opmodel')
    slug = models.SlugField(null=False, unique=True)  # new

    # def goals(self):
    #     return ModelGoal.objects.get(model=self)

    def region(self):
        """
        Add Compuational Region
        """
        pass

    def scenarios_count():
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("opmodel_detail", kwargs={"slug": self.slug})

    def _create_location(self):
        print("Creating Mapset: ", self.slug)
        client = acp.initActiniaClient()  # Add the users credentials
        location_name = self.slug.replace('-', '_')
        self.location = location_name
        client.create_location(location_name, 5070)
        locations = client.get_locations()
        print("Locations", locations)
        mapsets = locations[location_name].get_mapsets()
        print("Mapsets", mapsets)
        mapset_name = self.owner.username
        locations[location_name].create_mapset(mapset_name)
        self.mapset = mapset_name

    def save(self, *args, **kwargs):  # new
        print("SAVE: Creating new modeling object with override on the model")
        if not self.slug:
            self.slug = slugify(self.name)
            print("slug:", self.slug)
        if not self.location:
            self._create_location()
        return super().save(*args, **kwargs)

    def create(self, *args, **kwargs):  # new
        print("CREATE: Creating new modeling object with override on the model")
        if not self.slug and self.location:
            self.slug = slugify(self.name)
        if not self.location:
            self._create_location()
        return super().create(*args, **kwargs)

    def _list_counties_geoid(self):
        """Generate list of counties geoids"""
        counties = self.counties.all()
        countyIds = map(str, [c.county.geoid for c in counties])
        return countyIds

    def geoids(self):
        """Create geoid SQL where query for Actinia county import"""
        countyIds = self._list_counties_geoid()
        geoids = "geoid in ("
        for c, v in enumerate(countyIds):
            if (c == 0):
                geoids = geoids + f"'{v}'"
            else:
                geoids = geoids + f",'{v}'"
        geoids = geoids + ")"
        return geoids

    def model_region_centroid(self, epsg=3358):
        """Returns the centroid of the region of interest"""
        county_geoids = self._list_counties_geoid()
        centroid = County.objects.filter(geoid__in=county_geoids).aggregate(point=Centroid(Union('geom')))

        return centroid
