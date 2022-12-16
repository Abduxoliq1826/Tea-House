from django.shortcuts import render, redirect
from main.models import *
from main.views import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import date


@login_required(login_url='sign-in')
def director_dashboard(request):
    user = request.user
    if user.type == 1:
        total_price = 0
        for i in Order.objects.filter(done=True):
            total_price += i.total_price
        context = {
            'total_order': Order.objects.filter(done=True).count(),
            'total_price': total_price,
            'users': User.objects.all().count(),
            'client': Client.objects.all().count(),

        }
        return render(request, 'director/index.html', context)
    else:
        return redirect('sign-in')


# user

@login_required(login_url='sign-in')
def users(request):
    user = request.user
    if user.type == 1:
        if request.method == "POST":
            search = request.POST.get('search')
            search_rezult = User.objects.filter(username__icontains=search)
            context = {
                'users': search_rezult,
            }
            return render(request, 'director/users.html',context)
        context = {
            'users': User.objects.all(),
        }
        return render(request, 'director/users.html',context)
    else:
        return redirect('sign-in')
@login_required(login_url='sign-in')
def add_user(request):
    user = request.user
    if user.type == 1:
        username = request.POST.get('username')
        password = request.POST.get('password')
        type = request.POST.get('type')
        number = request.POST.get('number')
        User.objects.create_user(username=username, password=password, type=int(type), number=number)
        return redirect('users')
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def update_user(request, pk):
    user = request.user
    if user.type == 1:
        context = {
            'user': User.objects.get(id=pk),
        }
        if request.method == "POST":
            user = User.objects.get(id=pk)
            type = request.POST.get('type')
            username = request.POST.get('username')
            image = request.FILES.get('image')
            number = request.POST.get('number')
            password = request.POST.get('password')
            user.username = username
            user.number = number
            if image is None:
                user.image = user.image
            else:
                user.image = image

            if type == 0:
                user.type = user.type
            else:
                user.type = type
            if password is None:
                user.set_password(user.password)
            else:
                user.set_password(password)
            user.save()
            return redirect('users')
        return render(request, 'director/update_user.html', context)
    else:
        return redirect('sign-in')


def delete_user(request, pk):
    user = request.user
    if user.type == 1:
        user = User.objects.get(id=pk)
        user.delete()
        return redirect('users')
    else:
        return redirect('sign-in')



# client

@login_required(login_url='sign-in')
def clients(request):
    user = request.user
    if user.type == 1:
        if request.method == "POST":
            search = request.POST.get('search')
            search_rezult = Client.objects.filter(name__icontains=search)
            context = {
                'clients': search_rezult,
            }
            return render(request, 'director/clients.html', context)
        context = {
            'clients': Client.objects.all(),
        }
        return render(request, 'director/clients.html', context)
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def add_client(request):
    user = request.user
    if user.type == 1:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        Client.objects.create(name=name, phone=phone)
        return redirect('clients')
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def update_client(request, pk):
    user = request.user
    if user.type == 1:
        client = Client.objects.get(id=pk)
        context = {
            'user': user,
            'client': client,
        }
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            client.name = name
            client.phone = phone
            client.save()
            return redirect('clients')
        return render(request, "director/update_client.html", context)
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def delete_client(request, pk):
    user = request.user
    if user.type == 1:
        client = Client.objects.get(id=pk)
        client.delete()
        return redirect('clients')
    else:
        return redirect('sign-in')

# Room



@login_required(login_url='sign-in')
def rooms(request):
    user = request.user
    if user.type == 1:
        if request.method == "POST":
            search = request.POST.get('search')
            search_rezult = Room.objects.filter(number__icontains=search)
            context = {
                'room': search_rezult,
            }
            return render(request, 'director/rooms.html', context)
        context = {
            'room': Room.objects.all(),
        }
        return render(request, 'director/rooms.html', context)
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def add_room(request):
    user = request.user
    if user.type == 1:
        number = request.POST['number']
        people = request.POST['people']
        Room.objects.create(number=number, people=people)
        return redirect('rooms')
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def update_room(request, pk):
    user = request.user
    if user.type == 1:
        room = Room.objects.get(id=pk)
        context = {
            'room': room,
            'user': user
        }
        if request.method == "POST":
            number = request.POST.get('number')
            people = request.POST.get('people')
            room.number = number
            room.people = people
            room.save()
            return redirect('rooms')
        return render(request, "director/update_room.html", context)
    else:
        return redirect('sign-in')

def delete_room(request, pk):
    user = request.user
    if user.type == 1:
        room = Room.objects.get(id=pk)
        room.delete()
        return redirect('rooms')
    else:
        return redirect('sign-in')


# maxsulot

@login_required(login_url='sign-in')
def maxsulot(request):
    user = request.user
    if user.type == 1:
        if request.method == "POST":
            search = request.POST.get('search')
            search_rezult = Maxsulot.objects.filter(name__icontains=search)
            context = {
                'maxsulot': search_rezult,
            }
            return render(request, 'director/maxsulot.html', context)
        context = {
            'maxsulot': Maxsulot.objects.all(),
        }
        return render(request, 'director/maxsulot.html', context)
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def add_maxsulot(request):
    user = request.user
    if user.type == 1:
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        price = request.POST.get('price')
        Maxsulot.objects.create(quantity=quantity, name=name, price=price)
        return redirect('maxsulot')
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def update_maxsulot(request, pk):
    user = request.user
    if user.type == 1:
        maxsulot = Maxsulot.objects.get(id=pk)
        context = {
            'maxsulot': maxsulot,
            'user': user
        }
        if request.method == 'POST':
            quantity = request.POST.get('quantity')
            name = request.POST.get('name')
            price = request.POST.get('price')
            maxsulot.quantity = quantity
            maxsulot.name = name
            maxsulot.price = price
            maxsulot.save()
            return redirect('maxsulot')
        return render(request, 'director/order_item.html', context)
    else:
        return redirect('sign-in')


def delete_maxsulot(request, pk):
    user = request.user
    if user.type == 1:
        maxsulot = Maxsulot.objects.get(id=pk)
        maxsulot.delete()
        return redirect('maxsulot')
    else:
        return redirect('sign-in')
@login_required(login_url='sign-in')
def check_maxsulot(request, pk):
    user = request.user
    if user.type == 1:
        meal = Maxsulot.objects.get(id=pk)
        if meal.is_yes == False:
            meal.is_yes = True
            meal.save()
        else:
            meal.is_yes = False
            meal.save()
        return redirect('maxsulot')
    else:
        return redirect('sign-in')


# meal

@login_required(login_url='sign-in')
def meal(request):
    user = request.user
    if user.type == 1:
        if request.method == "POST":
            search = request.POST.get('search')
            search_rezult = Meal.objects.filter(name__icontains=search)
            context = {
                'meal': search_rezult,
            }
            return render(request, 'director/meal.html', context)
        context = {
            'meal': Meal.objects.all(),
        }
        return render(request, 'director/meal.html', context)
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def add_meal(request):
    user = request.user
    if user.type == 1:
        name = request.POST.get('name')
        price = request.POST.get('price')
        Meal.objects.create(name=name, price=price)
        return redirect('meal')
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def update_meal(request, pk):
    user = request.user
    if user.type == 1:
        meal = Meal.objects.get(id=pk)
        context = {
            'meal': meal,
            'user': user
        }
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            meal.name = name
            meal.price = price
            meal.save()
            return redirect('meal')
        return render(request, 'director/update_meal.html', context)
    else:
        return redirect('sign-in')

def delete_meal(request, pk):
    user = request.user
    if user.type == 1:
        meal = Meal.objects.get(id=pk)
        meal.delete()
        return redirect('meal')
    else:
        return redirect('sign-in')



@login_required(login_url='sign-in')
def check_meal(request, pk):
    user = request.user
    if user.type == 1:
        meal = Meal.objects.get(id=pk)
        if meal.is_yes == False:
            meal.is_yes = True
            meal.save()
        else:
            meal.is_yes = False
            meal.save()
        return redirect('meal')
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def profile(request):
    user = request.user
    if user.type == 1:
        context = {
            'user': user,
        }
        if request.method == "POST":
            type = request.POST.get('type')
            username = request.POST.get('username')
            image = request.FILES.get('image')
            number = request.POST.get('number')
            password = request.POST.get('password')
            user.username = username
            user.number = number
            if image is None:
                user.image = user.image
            else:
                user.image = image

            if type == 0:
                user.type = user.type
            else:
                user.type = type

            if password is None:
                user.set_password(user.password)
            else:
                user.set_password(password)
            user.save()
            return redirect('director_profile')

        return render(request, 'director/profile.html', context)

    else:
        return redirect('sign-in')



# meal

@login_required(login_url='sign-in')
def orders(request):
    user = request.user
    if user.type == 1:
        if request.method == "POST":
            search = request.POST.get('search')
            search_rezult = Order.objects.filter(date__icontains=search)
            context = {
                'order': search_rezult,
            }
            return render(request, 'director/orders.html', context)

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
        return render(request, 'director/orders.html', context)
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def add_delivery(request):
    user = request.user
    if user.type == 1:
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
        return redirect('orders')
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def add_orders(request):
    user = request.user
    if user.type == 1:
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
        return redirect('orders')
    else:
        return redirect('sign-in')



@login_required(login_url='sign-in')
def update_order(request, pk):
    user = request.user
    if user.type == 1:
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
            return redirect('orders')
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
        return render(request, 'director/update_order.html', context)
    else:
        return redirect('sign-in')


@login_required(login_url='sign-in')
def update_delivery(request, pk):
    user = request.user
    if user.type == 1:
        address = request.POST.get('address')
        delivery_date = request.POST.get('delivery_date')
        owner = request.POST.get('owner')
        order = Order.objects.get(id=pk)
        order.address = address
        order.delivery_date = delivery_date
        order.owner = Client.objects.get(id=owner)
        order.save()
        return redirect('orders')
    else:
        return redirect('sign-in')



@login_required(login_url='sign-in')
def delete_order(request, pk):
    user = request.user
    if user.type == 1:
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect('orders')
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def Add_order_item(request, pk):
    user = request.user
    if user.type == 1:
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
            return redirect('director_order_item')
        return render(request, 'director/add_order_item.html', con)
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def Update_order_item(request, pk):
    user = request.user
    if user.type == 1:
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
            return redirect('director_order_item')
        con = {
            'pk': pk,
            'orders': OrderItem.objects.get(id=pk),
            'maxsulot': Maxsulot.objects.filter(is_yes=True).order_by('-id'),
            'meal': Meal.objects.filter(is_yes=True).order_by('-id')
        }
        return render(request, 'director/update_order_item.html', con)
    else:
        return redirect('sign-in')



def Done_order(request, pk):
    user = request.user
    if user.type == 1:
        order = Order.objects.get(id=pk)
        if user.type == 3:
            if order.done == False:
                order.done = True
                order.save()
        return redirect('orders')
    else:
        return redirect('sign-in')

@login_required(login_url='sign-in')
def Order_items(request):
    user = request.user
    if user.type == 1:
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
        return render(request, 'director/order_item.html', con)
    else:
        return redirect('sign-in')
@login_required(login_url='sign-in')
def Orders(request):
    user = request.user
    if user.type == 1:
        context = {
            'order': Order.objects.filter(delivery=False, done=False),
            'delivery': Order.objects.filter(delivery=True, done=False),
        }
        return render(request, 'director/order.html', context)
    else:
        return redirect('sign-in')