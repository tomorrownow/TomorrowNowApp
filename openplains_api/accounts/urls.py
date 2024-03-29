###############################################################################
# Filename: urls.py                                                            #
# Project: TomorrowNow                                                         #
# File Created: Tuesday May 31st 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Fri Oct 14 2022                                               #
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


from django.urls import path
# from django.conf.urls import url
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('users/', views.UserCreate.as_view(), name='account-create'),
    # path('api/users/<user_id>', views.UserCreate.as_view(), name='account-create'),
    # path('users/current/profile/', views.UserProfile.as_view(), name='user-profile'),
    path('users/<str:user_id>/profile/', views.UserProfile.as_view(), name='user-profile'),
]
