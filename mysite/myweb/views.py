from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    return render(req, 'myweb/base.html')

def Login(request):

    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == 'POST' :
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('')

                else:
                    messages.info(request, 'Username or Password is incorrect')


            except:
                messages.error(request, 'Username not found')
        context = {}
        return render(request, 'myweb/login.html', context)

def Logout(req):
    user_logout(req)
    return redirect('')
#@Login_required(login_url='login')

