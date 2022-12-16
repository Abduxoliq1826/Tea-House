from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('call_center_index',call_center_index, name='call_center_index'),
    path('orders', orders, name='call_center_orders'),
    path('update_orders/<int:pk>', update_order, name='call_center_update_orders'),
    path('add_delivery', add_delivery, name='call_center_add_delivery'),
    path('add_orders', add_orders, name='call_center_add_orders'),
    path('update_delivery/<int:pk>', update_delivery, name='call_center_update_delivery'),

    path('order/', Orders, name='call_center_order'),
    path('order_items/', Order_items, name='call_center_order_item'),
    path('add_order_item/<int:pk>/', Add_order_item, name='call_center_add_order_item'),
    path('done_order/<int:pk>/', Done_order, name='call_center_done_order'),
    path('update_order_item/<int:pk>/', Update_order_item, name='call_center_update_order_item'),
]