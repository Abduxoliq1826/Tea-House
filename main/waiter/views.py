from datetime import date
from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign-in')
def Index(request):
    return render(request, 'waiter/index.html')

@login_required(login_url='sign-in')
def Orders(request):
    context = {
        'order': Order.objects.filter(delivery=False, done=False),
        'delivery': Order.objects.filter(delivery=True, done=False),
    }
    return render(request, 'waiter/orders.html', context)


@login_required(login_url='sign-in')
def Order_items(request):
    con = {
        'user': request.user,
        'order_item': OrderItem.objects.all().order_by('-id')
    }
    return render(request, 'waiter/order_item.html', con)



@login_required(login_url='sign-in')
def Add_order_item(request, pk):
    user = request.user
    con = {
        'pk': pk,
        'order': Order.objects.get(id=pk),
        'maxsulot': Maxsulot.objects.filter(is_yes=True).order_by('-id'),
        'meal': Meal.objects.filter(is_yes=True).order_by('-id')
    }
    if user.type == 3:
        if request.method == 'POST':
            order = Order.objects.get(id=pk)
            maxsulot = request.POST.get('maxsulot')
            quantity = request.POST.get('quantity')
            meal = request.POST.get('meal')
            meal_quantity = request.POST.get('meal_quantity')
            OrderItem.objects.create(order_id=order.id, maxsulot_id=maxsulot, quantity=quantity, meal_id=meal, meal_quantity=meal_quantity)
            return redirect('order')
    return render(request, 'waiter/add_order_item.html', con)


@login_required(login_url='sign-in')
def Update_order_item(request, pk):
    con = {
        'pk': pk,
        'orders': OrderItem.objects.get(id=pk),
        'maxsulot': Maxsulot.objects.filter(is_yes=True).order_by('-id'),
        'meal': Meal.objects.filter(is_yes=True).order_by('-id')
    }
    user = request.user
    order = OrderItem.objects.get(id=pk)
    if user.type == 3:
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
            return redirect('order_item')
    return render(request, 'waiter/update_order_item.html', con)

def Done_order(request, pk):
    user = request.user
    order = Order.objects.get(id=pk)
    if user.type == 3:
        if order.done == False:
            order.done = True
            order.save()
    return redirect('order')



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
        return redirect('waiter_profile')
    return render(request, 'waiter/profile.html', context)


