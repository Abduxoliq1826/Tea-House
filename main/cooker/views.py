from datetime import date
from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign-in')
def cooker_dashboard(request):
    total_price = 0
    for i in Order.objects.filter(done=True):
        total_price += i.total_price
    context = {
        'total_order': Order.objects.filter(done=True).count(),
        'total_price': total_price,
        'users': User.objects.all().count(),
        'client': Client.objects.all().count(),

    }
    return render(request, 'cooker/index.html', context)


@login_required(login_url='sign-in')
def order(request):
    context = {
        'order': Order.objects.filter(done=False),
    }
    return render(request, 'cooker/orders.html', context)


@login_required(login_url='sign-in')
def order_item(request):
    context = {
        'order_item': OrderItem.objects.filter(order__done=False),
    }
    return render(request, 'cooker/order_item.html', context)

# meal


@login_required(login_url='sign-in')
def meal(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_rezult = Meal.objects.filter(name__icontains=search)
        context = {
            'meal': search_rezult,
        }
        return render(request, 'cooker/meal.html', context)
    context = {
        'meal': Meal.objects.all(),
    }
    return render(request, 'cooker/meal.html', context)




@login_required(login_url='sign-in')
def add_meal(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    Meal.objects.create(name=name, price=price)
    return redirect('cooker_meal')


@login_required(login_url='sign-in')
def update_meal(request, pk):
    user = request.user
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
        return redirect('cooker_meal')
    return render(request, 'cooker/update_meal.html', context)


def delete_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    meal.delete()
    return redirect('cooker_meal')

@login_required(login_url='sign-in')
def check_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    if meal.is_yes == False:
        meal.is_yes = True
        meal.save()
    else:
        meal.is_yes = False
        meal.save()
    return redirect('cooker_meal')





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
        return redirect('cooker_profile')
    return render(request, 'cooker/profile.html', context)