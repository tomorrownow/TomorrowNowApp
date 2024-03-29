###############################################################################
# Filename: routing.py                                                         #
# Project: TomorrowNow                                                         #
# File Created: Sunday March 27th 2022                                         #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Tue Nov 22 2022                                               #
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

from django.urls import re_path, path
# from django.conf.urls import url

# from channels.routing import ProtocolTypeRouter, URLRouter


# from . import consumers
from .consumers import ActiniaResourceConsumer

websocket_urlpatterns = [
    # re_path(r'ws/savana/resource/(?P<resource_id>\w+)/$', consumers.ActiniaResourceConsumer.as_asgi()),
    re_path(r'ws/savana/resource/(?P<resource_name>\w+)/$', ActiniaResourceConsumer.as_asgi())
    # re_path(r'ws/savana/resource/(?P<resource_id>\w+)/$', consumers.ActiniaResourceConsumer.as_asgi()),

    # url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),

]
