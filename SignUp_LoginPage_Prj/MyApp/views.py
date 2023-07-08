from django.shortcuts import render
from .forms import SignUpForm, UserProfileForm, EditAdminProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User
# Create your views here.


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request, "Account has been created successfully")
        else:
            fm = SignUpForm()
        return render(request, 'MyApp/signup.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/profile/')


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
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'MyApp/login.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = UserProfileForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile Updated Successfully")
        else:
            if request.user.is_superuser:
                users = User.objects.all()
                fm = EditAdminProfileForm(request.POST, instance=request.user)
            else:
                fm = UserProfileForm(instance=request.user)
                users = None
        return render(request, 'MyApp/profile.html', {'name': request.user.first_name, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def Logout(request):
    fm = logout(request)
    return HttpResponseRedirect('/login/')


def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "password changed successfully")
                update_session_auth_hash(request, request.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'MyApp/passwordchange.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/login/')


def UserDetails(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(id=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'MyApp/userdetails.html', {"form": fm})
    else:
        return HttpResponseRedirect('/login/')
