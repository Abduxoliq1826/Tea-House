from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', director_dashboard, name='director_dashboard'),
    path('profile', profile, name='director_profile'),

    # user
    path('user', users, name='users'),
    path('add_user', add_user, name='add_user'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
    path('update_user/<int:pk>', update_user, name='update_user'),


    # client
    path('clients', clients, name='clients'),
    path('add_client', add_client, name='add_client'),
    path('delete_client/<int:pk>', delete_client, name='delete_client'),
    path('update_client/<int:pk>', update_client, name='update_client'),



    # room
    path('rooms', rooms, name='rooms'),
    path('add_room', add_room, name='add_room'),
    path('delete_room/<int:pk>', delete_room, name='delete_room'),
    path('update_room/<int:pk>', update_room, name='update_room'),



    # maxsulot
    path('maxsulot', maxsulot, name='maxsulot'),
    path('add_maxsulot', add_maxsulot, name='add_maxsulot'),
    path('delete_maxsulot/<int:pk>', delete_maxsulot, name='delete_maxsulot'),
    path('update_maxsulot/<int:pk>', update_maxsulot, name='update_maxsulot'),
    path('check_maxsulot/<int:pk>', check_maxsulot, name='check_maxsulot'),



    # meal
    path('meal', meal, name='meal'),
    path('add_meal', add_meal, name='add_meal'),
    path('delete_meal/<int:pk>', delete_meal, name='delete_meal'),
    path('update_meal/<int:pk>', update_meal, name='update_meal'),
    path('check_meal/<int:pk>', check_meal, name='check_meal'),


    # order
    path('orders', orders, name='orders'),
    path('add_delivery', add_delivery, name='add_delivery'),
    path('add_order', add_orders, name='add_order'),
    path('update_order/<int:pk>', update_order, name='update_order'),
    path('update_delivery/<int:pk>', update_delivery, name='update_delivery'),
    path('delete_order/<int:pk>', delete_order, name='delete_order'),


    path('order/', Orders, name='director_order'),
    path('order_items/', Order_items, name='director_order_item'),
    path('add_order_item/<int:pk>/', Add_order_item, name='director_add_order_item'),
    path('done_order/<int:pk>/', Done_order, name='director_done_order'),
    path('update_order_item/<int:pk>/', Update_order_item, name='director_update_order_item'),
]