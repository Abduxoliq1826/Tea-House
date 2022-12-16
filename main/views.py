from datetime import date
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .director.views import *


def cooker_dashboard(request):
    return render(request, 'cooker/index.html')


def waiter_dashboard(request):
    return render(request, 'waiter/index.html')


def manager_dashboard(request):
    return render(request, 'manager/index.html')


def call_center_dashboard(request):
    return render(request, 'call_center/index.html')


def Sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user2 = User.objects.filter(username=username)
        if user2 is not None:
            user1 = User.objects.get(username=username)
            usr = authenticate(username=username, password=password)
            if usr is not None:
                if user1.type == 1:
                    login(request, usr)
                    return redirect('director_dashboard')
                elif user1.type == 2:
                    login(request, usr)
                    return redirect('cooker_dashboard')
                elif user1.type == 3:
                    login(request, usr)
                    return redirect('waiter_index')
                elif user1.type == 4:
                    login(request, usr)
                    return redirect('manager_dashboard')
                else:
                    login(request, usr)
                    return redirect('call_center_index')
            else:
                return redirect('sign-in')
        else:
            return redirect('sign-in')
    else:
        return render(request, 'sign-in.html')



def LogOut(request):
    logout(request)
    return redirect('sign-in')

