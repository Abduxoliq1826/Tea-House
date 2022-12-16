from datetime import date
from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign-in')
def call_center_index(request):
    return render(request, 'call_center/index.html')

@login_required(login_url='sign-in')
def orders(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_rezult = Order.objects.filter(date__icontains=search, delivery_date__icontains=search)
        context = {
            'order': search_rezult,
        }
        return render(request, 'call_center/orders.html', context)

    d1 = date.today()
    r = Room.objects.all()
    order = Order.objects.filter(date=d1, done=False)
    free = []
    for i in r:
        free.append(i)
    for x in free:
        for i in order:
            if i.room == x:
                free.remove(x)
    context = {
        'order': Order.objects.all(),
        'room': free,
    }
    return render(request, 'call_center/orders.html', context)


@login_required(login_url='sign-in')
def add_delivery(request):
    owner = {}
    phone = request.POST.get('phone')
    name = request.POST.get('name')
    address = request.POST.get('address')
    delivery_date = request.POST.get('delivery_date')
    a = 0
    for i in Client.objects.all():
        if int(phone) == i.phone:
            owner = i
            a += 1
        else:
            a += 0
    if a == 0:
        owner = Client.objects.create(phone=phone, name=name)
    else:
        pass

    Order.objects.create(owner_id=owner.id, delivery_date=delivery_date, address=address, delivery=True)
    return redirect('call_center_orders')



@login_required(login_url='sign-in')
def add_orders(request):
    phone = request.POST.get('phone')
    name = request.POST.get('name')
    room = request.POST.get('room')
    date = request.POST.get('date')
    rooms = Room.objects.get(id=room)
    rooms.is_free = False
    rooms.save()
    a = 0
    for i in Client.objects.all():
        if int(phone) == i.phone:
            owner = i
            a += 1
        else:
            pass
    if a == 1:
        pass
    else:
        owner = Client.objects.create(phone=phone, name=name)
    Order.objects.create(delivery=False, room_id=room, date=date, owner=owner)
    return redirect('call_center_orders')




@login_required(login_url='sign-in')
def update_order(request, pk):

    global date
    if request.method == "POST":
        room = request.POST.get('room')
        date = request.POST.get('date')
        owner = request.POST.get('owner')
        order = Order.objects.get(id=pk)
        order.date = date
        order.owner_id = owner
        order.room = Room.objects.get(id=room)
        order.save()
        return redirect('call_center_orders')
    d1 = date.today()
    r = Room.objects.all()
    order = Order.objects.filter(date=d1, done=False)
    free = []
    for i in r:
        free.append(i)
    for x in free:
        for i in order:
            if i.room == x:
                free.remove(x)
    context = {
        'room': free,
        'order': Order.objects.get(id=pk),
        'owner': Client.objects.all()
    }
    return render(request, 'call_center/update_order.html', context)



@login_required(login_url='sign-in')
def update_delivery(request, pk):
    address = request.POST.get('address')
    delivery_date = request.POST.get('delivery_date')
    owner = request.POST.get('owner')
    order = Order.objects.get(id=pk)
    order.address = address
    order.delivery_date = delivery_date
    order.owner = Client.objects.get(id=owner)
    order.save()
    return redirect('call_center_orders')



@login_required(login_url='sign-in')
def Add_order_item(request, pk):
    user = request.user
    con = {
        'pk': pk,
        'order': Order.objects.get(id=pk),
        'maxsulot': Maxsulot.objects.filter(is_yes=True).order_by('-id'),
        'meal': Meal.objects.filter(is_yes=True).order_by('-id')
    }
    if request.method == "POST":
        order = Order.objects.get(id=pk)
        maxsulot = request.POST.get('maxsulot')
        quantity = request.POST.get('quantity')
        meal = request.POST.get('meal')
        meal_quantity = request.POST.get('meal_quantity')
        OrderItem.objects.create(order=order, maxsulot=Maxsulot.objects.get(id=maxsulot), quantity=quantity, meal=Meal.objects.get(id=meal), meal_quantity=meal_quantity)
        return redirect('call_center_order_item')
    return render(request, 'call_center/add_order_item.html', con)


@login_required(login_url='sign-in')
def Update_order_item(request, pk):
    user = request.user
    order = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        maxsulot = request.POST.get('maxsulot')
        quantity = request.POST.get('quantity')
        meal = request.POST.get('meal')
        meal_quantity = request.POST.get('meal_quantity')
        if maxsulot == None:
            order.maxsulot = order.maxsulot
        else:
            order.maxsulot = maxsulot
        order.quantity = quantity
        if maxsulot == None:
            order.meal = order.meal
        else:
            order.meal = meal
        order.meal_quantity = meal_quantity
        order.save()
        return redirect('call_center_order_item')
    con = {
        'pk': pk,
        'orders': OrderItem.objects.get(id=pk),
        'maxsulot': Maxsulot.objects.filter(is_yes=True).order_by('-id'),
        'meal': Meal.objects.filter(is_yes=True).order_by('-id')
    }
    return render(request, 'call_center/update_order_item.html', con)

def Done_order(request, pk):
    user = request.user
    order = Order.objects.get(id=pk)
    if order.done == False:
        order.done = True
        order.save()
    return redirect('call_center_orders')


@login_required(login_url='sign-in')
def Order_items(request):
    d1 = date.today()
    r = Room.objects.all()
    order = Order.objects.filter(date=d1, done=False)
    free = []
    for i in r:
        free.append(i)
    for x in free:
        for i in order:
            if i.room == x:
                free.remove(x)
    con = {
        'room': free,
        'user': request.user,

        'order_item': OrderItem.objects.all().order_by('-id')
    }
    return render(request, 'call_center/order_item.html', con)

@login_required(login_url='sign-in')
def Orders(request):
    context = {
        'order': Order.objects.filter(delivery=False, done=False),
        'delivery': Order.objects.filter(delivery=True, done=False),
    }
    return render(request, 'call_center/order.html', context)
