from datetime import date
from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url='sign-in')
def manager_dashboard(request):
    return render(request, 'manager/index.html')



# user

@login_required(login_url='sign-in')
def users(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_rezult = User.objects.filter(username__icontains=search)
        context = {
            'users': search_rezult,
        }
        return render(request, 'manager/users.html',context)
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'manager/users.html',context)


@login_required(login_url='sign-in')
def add_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    type = request.POST.get('type')
    number = request.POST.get('number')
    User.objects.create_user(username=username, password=password, type=type, number=number)
    return redirect('manager_user')


@login_required(login_url='sign-in')
def update_user(request, pk):
    context = {
        'user': User.objects.get(id=pk)
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
        return redirect('manager_add_user')
    return render(request, 'manager/update_user.html', context)



def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('manager_user')




# client


@login_required(login_url='sign-in')
def clients(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_rezult = Client.objects.filter(name__icontains=search)
        context = {
            'clients': search_rezult,
        }
        return render(request, 'manager/clients.html', context)
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, 'manager/clients.html', context)




@login_required(login_url='sign-in')
def add_client(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    Client.objects.create(name=name, phone=phone)
    return redirect('manager_clients')

@login_required(login_url='sign-in')
def update_client(request, pk):
    client = Client.objects.get(id=pk)
    context = {
        'client': client,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        client.name = name
        client.phone = phone
        client.save()
        return redirect('manager_clients')
    return render(request, "manager/update_client.html", context)


def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect('manager_clients')


# Room


@login_required(login_url='sign-in')
def rooms(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_rezult = Room.objects.filter(number__icontains=search)
        context = {
            'room': search_rezult,
        }
        return render(request, 'manager/rooms.html', context)
    context = {
        'room': Room.objects.all(),
    }
    return render(request, 'manager/rooms.html', context)





@login_required(login_url='sign-in')
def add_room(request):
        number = request.POST['number']
        people = request.POST['people']
        Room.objects.create(number=number, people=people)
        return redirect('manager_rooms')

@login_required(login_url='sign-in')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        'room': room,
    }
    if request.method == "POST":
        number = request.POST.get('number')
        people = request.POST.get('people')
        room.number = number
        room.people = people
        room.save()
        return redirect('manager_rooms')
    return render(request, "manager/update_room.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return redirect('manager_rooms')



# maxsulot


@login_required(login_url='sign-in')
def maxsulot(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_rezult = Maxsulot.objects.filter(name__icontains=search)
        context = {
            'maxsulot': search_rezult,
        }
        return render(request, 'manager/maxsulot.html', context)
    context = {
        'maxsulot': Maxsulot.objects.all(),
    }
    return render(request, 'manager/maxsulot.html', context)



@login_required(login_url='sign-in')
def add_maxsulot(request):
    quantity = request.POST.get('quantity')
    name = request.POST.get('name')
    price = request.POST.get('price')
    Maxsulot.objects.create(quantity=quantity, name=name, price=price)
    return redirect('manager_maxsulot')


@login_required(login_url='sign-in')
def update_maxsulot(request, pk):
    maxsulot = Maxsulot.objects.get(id=pk)
    context = {
        'maxsulot': maxsulot
    }
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        price = request.POST.get('price')
        maxsulot.quantity = quantity
        maxsulot.name = name
        maxsulot.price = price
        maxsulot.save()
        return redirect('manager_maxsulot')
    return render(request, 'manager/update_maxsulot.html', context)

def delete_maxsulot(request, pk):
    maxsulot = Maxsulot.objects.get(id=pk)
    maxsulot.delete()
    return redirect('manager_maxsulot')

@login_required(login_url='sign-in')
def add_order(request):
    user = request.user
    context = {
        'order': Order.objects.all()
    }
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        price = request.POST.get('price')
        Maxsulot.objects.create(quantity=quantity, name=name, price=price)
        return render(request, 'manager/orders.html', context)
    return render(request, 'manager/orders.html', context)

@login_required(login_url='sign-in')
def check_maxsulot(request, pk):
    meal = Maxsulot.objects.get(id=pk)
    if meal.is_yes == False:
        meal.is_yes = True
        meal.save()
    else:
        meal.is_yes = False
        meal.save()
    return redirect('manager_maxsulot')




@login_required(login_url='sign-in')
def profile(request):
    user = request.user
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
        return redirect('manager_profile')
    return render(request, 'manager/profile.html', context)


