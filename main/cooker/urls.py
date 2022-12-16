from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('', cooker_dashboard, name='cooker_dashboard'),
    path('profile', profile, name='cooker_profile'),



    # check
    path('meal', meal, name='cooker_meal'),
    path('add_meal', add_meal, name='cooker_add_meal'),
    path('update_meal/<int:pk>', update_meal, name='cooker_update_meal'),
    path('delete_meal/<int:pk>', delete_meal, name='cooker_delete_meal'),
    path('check_meal/<int:pk>', check_meal, name='cooker_check_meal'),



    path('order', order, name='cooker_order'),
    path('order_item', order_item, name='cooker_order_item'),




]