from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('order_items/', Order_items, name='order_item'),
    path('order/', Orders, name='order'),
    path('index/', Index, name='waiter_index'),
    path('add_order_item/<int:pk>/', Add_order_item, name='add_order_item'),
    path('done_order/<int:pk>/', Done_order, name='done_order'),
    path('update_order_item/<int:pk>/', Update_order_item, name='update_order_item'),
    path('profile', profile, name='waiter_profile'),
]