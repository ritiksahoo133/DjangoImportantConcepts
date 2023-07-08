from django.shortcuts import render
from .forms import SignUpForm, UserProfileForm, EditAdminProfileForm
from django.http import HttpResponseRedirect
from .models import blog
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User, Group
# Create your views here.


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                user = request.user
                group = Group.objects.get(name="Editor")
                user.groups.add(group)
                messages.success(
                    request, "Account has been created successfully")
        else:
            fm = SignUpForm()
        return render(request, 'MyApp/signup.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    print(user)
                    messages.success(request, "You are Logged in")
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'MyApp/login.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'MyApp/dashboard.html', {'name': request.user.username})
    else:
        return HttpResponseRedirect('/login/')


def Logout(request):
    fm = logout(request)
    return HttpResponseRedirect('/login/')
