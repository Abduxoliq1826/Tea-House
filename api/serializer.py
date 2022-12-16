from rest_framework import serializers
from main.models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maxsulot
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"

class BotinfoSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = BotDetail
        fields = "__all__"
