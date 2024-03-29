###############################################################################
# Filename: DrainRequest.py                                                    #
# Project: TomorrowNow                                                         #
# File Created: Wednesday April 13th 2022                                      #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Sat Nov 05 2022                                               #
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


# from django.db import models
from django.contrib.gis.db import models


class DrainRequest(models.Model):
    # id = models.AutoField()
    created = models.DateTimeField(auto_now_add=True)
    point = models.PointField(srid=4326)
    huc12 = models.CharField(max_length=250, null=True)  # convert this to ForeignKey later.
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='watershed_analysis', null=True)
    # Returns the string representation of the model.

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
