from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('rooms/', BotRooms),
    path('meals/', BotMeals),
    path('product/', Product),
    path('delivery/', Delivery_create),
    path('order/', Create_order),
    path('info/', BotInfo),
    path('detail/', BotDetaill),
]