###############################################################################
# Filename: OpenModelExtent.py                                                 #
# Project: TomorrowNow                                                         #
# File Created: Monday October 17th 2022                                       #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Tue Oct 18 2022                                               #
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
from django.db import models


class ModelExtent(models.Model):
    """A feature representing part or all of a models extent"""

    model = models.ForeignKey("savana.OpenPlainsModel", editable=True, on_delete=models.CASCADE, null=False, related_name='counties')
    county = models.ForeignKey("world.County", editable=True, on_delete=models.CASCADE, null=False)

## SQL to get centroid and extent as geojson
#     WITH
# 	_region AS (
# 		SELECT
# 			geoid,
# 			geom
# 		FROM world_county as counties
# 		WHERE geoid in ('37183', '37063', '37135')
# 	)

# SELECT
# 	ST_ASGEOJSON(ST_CENTROID(ST_UNION(geom))) as centroid,
# 	ST_ASGEOJSON(ST_Extent(geom)) as extent
# FROM _region