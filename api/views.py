from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from .serializer import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def BotRooms(request):
    room = Room.objects.filter(is_free=False)
    return Response(RoomSerializer(room, many=True).data)

@api_view(['GET'])
def BotMeals(request):
    meal = Meal.objects.filter(is_yes=True)
    return Response(MealSerializer(meal,many=True).data)

@api_view(['GET'])
def Product(request):
    product = Maxsulot.objects.filter(is_yes=True)
    return Response(ProductSerializer(product, many=True).data)


@api_view(['POST'])
def Delivery_create(request):
    delivery = True
    owner = request.POST['owner']
    address = request.POST['address']
    date = request.POST['date']
    for i in Client.objects.all():
        if  i.name == owner:
            query = Order.objects.create(delivery=delivery, owner=i.name, address=address, delivery_date=date)
            data = {
                'owner': owner,
                'address': query.address,
                'date': query.delivery_date
            }
            return Response(data)
        else:
            client = Client.objects.create(name=owner)
            query = Order.objects.create(delivery=delivery, owner=client.name, address=address, delivery_date=date)
            data = {
                'owner': owner,
                'address': query.address,
                'date': query.delivery_date
            }
            return Response(data)

@api_view(['POST'])
def Create_order(request):
    room = request.POST['room']
    owner = request.POST['owner']
    date = request.POST['date']
    for i in Client.objects.all():
        if i.name == owner:
            print('hello')
            query = Order.objects.create(room_id=room,  owner=i.name, date=date)
            data = {
                'no'
                'owner': owner,
                'room': room,
                'date': date
            }
            return Response(data)
        elif owner != i.name:
            client = Client.objects.create(name=owner)
            query = Order.objects.create(room_id=room, owner=client.name, date=date)
            data = {
                'yes': query.delivery,
                'owner': owner,
                'room': room,
                'date': date
            }
            return Response(data)
@api_view(['GET'])
def BotInfo(request):
    info = Bot.objects.last()
    return Response(BotSerializer(info).data)

@api_view(['GET'])
def BotDetaill(reuest):
    detail = BotDetail.objects.last()
    return Response(BotinfoSerizlizer(detail).data)







