from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', manager_dashboard, name='manager_dashboard'),
    path('profile/', profile, name='manager_profile'),

    # user
    path('users/', users, name='manager_user'),
    path('add_user/', add_user, name='manager_add_user'),
    path('delete_user/<int:pk>/', delete_user, name='manager_delete_user'),
    path('update_user/<int:pk>/', update_user, name='manager_update_user'),


    # client
    path('clients/', clients, name='manager_clients'),
    path('add_client/', add_client, name='manager_add_client'),
    path('delete_client/<int:pk>/', delete_client, name='manager_delete_client'),
    path('update_client/<int:pk>/', update_client, name='manager_update_client'),



    # room
    path('rooms/', rooms, name='manager_rooms'),
    path('add_room/', add_room, name='manager_add_room'),
    path('delete_room/<int:pk>/', delete_room, name='manager_delete_room'),
    path('update_room/<int:pk>/', update_room, name='manager_update_room'),



    # maxsulot
    path('maxsulot/', maxsulot, name='manager_maxsulot'),
    path('add_maxsulot/', add_maxsulot, name='manager_add_maxsulot'),
    path('delete_maxsulot/<int:pk>/', delete_maxsulot, name='manager_delete_maxsulot'),
    path('update_maxsulot/<int:pk>/', update_maxsulot, name='manager_update_maxsulot'),
    path('check_maxsulot/<int:pk>/', check_maxsulot, name='manager_check_maxsulot'),






]