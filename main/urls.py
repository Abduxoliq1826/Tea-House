from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', Sign_in, name='sign-in'),
    path('logout', LogOut, name='logout'),
]