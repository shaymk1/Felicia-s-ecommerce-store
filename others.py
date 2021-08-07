from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from . models import *
from . forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import searchProfiles, paginateProfiles


# Create your views here.


def login_user(request):
    page = 'login'
    form = ProfileForm()
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']

        try:

            # checking if the username exist
            # email = User.objects.get(email=email)
            user = User.objects.get(username=username)
        except:

            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username,
                            password=password)  # check if they match

        if user is not None:
            # if user exist, log them in/create a session in the coockie for the user
            login(request, user)
            return redirect('profiles')

        else:

            messages.error(request, 'Username or Password incorrect')
    context = {

        'page': page,
        'form': form
    }
    return render(request, "users/login_register.html", context)


def logout_user(request):
    logout(request)
    messages.error(request, 'User was logged out successfully!')
    return redirect('login')
