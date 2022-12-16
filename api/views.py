from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from .serializer import *
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes(IsAuthenticated)
@authentication_classes([BasicAuthentication, SessionAuthentication])
def BotRooms(request):
    Room.objects.filter(is_free=False)
    return Response('')

@api_view(['GET'])
@permission_classes(IsAuthenticated)
@authentication_classes([ BasicAuthentication, SessionAuthentication])
def BotMeals(request):
    Meal.objects.filter(is_yes=True)
    return Response('')

@api_view(['GET'])
@permission_classes(IsAuthenticated)
@authentication_classes([ BasicAuthentication, SessionAuthentication])
def Product(request):
    Maxsulot.objects.filter(is_yes=True)
    return Response('')


@api_view(['GET'])
@permission_classes(IsAuthenticated)
@authentication_classes([ BasicAuthentication, SessionAuthentication])
def Delivery_create(request):
    delivery = True
    owner = request.POST['owner']
    address = request.POST['address']
    date = request.POST['date']
    Order.objects.create(delivery=delivery, owner=owner, address=address, date=date)
    return Response('')

@api_view(['GET'])
@permission_classes(IsAuthenticated)
@authentication_classes([ BasicAuthentication, SessionAuthentication])
def Create_order(request):






