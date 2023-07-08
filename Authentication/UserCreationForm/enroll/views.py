from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import signUp
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = signUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(
                request, "Account has been created successfully!!")

    else:
        fm = signUp()
    return render(request, 'enroll/home.html', {'form': fm})
