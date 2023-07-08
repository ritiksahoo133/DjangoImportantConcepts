from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUp, EditUserChangeForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.


def UserSignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUp(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request, "Account has been created successfully")
        else:
            fm = SignUp()
        return render(request, 'medicine/signup.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/profile/')


def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request.user, data=request.POST)
            print(request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(request, username=uname, password=password)
                print(user.username)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                messages.success('You are Logged in')
        else:
            fm = AuthenticationForm()
        return render(request, 'medicine/login.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserChangeForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'profile updated!!!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserChangeForm(instance=request.user)
                users = None
        return render(request, 'medicine/profile.html', {'name': request.user, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def Logout(request):
    fm = logout(request)
    return HttpResponseRedirect('/signup/')


def changePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "password changed successfully")
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
            print(fm.user)
        return render(request, 'medicine/changepassword.html', {'forms': fm})
    else:
        return HttpResponseRedirect('/login/')


def userdetails(request, id):
    if request.user.is_authenticated:
        id = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=id)
        return render(request, 'medicine/userdetails.html', {'fm': fm})
    else:
        return HttpResponseRedirect('/login/')
