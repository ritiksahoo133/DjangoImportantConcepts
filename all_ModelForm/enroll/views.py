from django.shortcuts import render
from .models import Student
from .forms import User


def home(request):
    fm = User()
    return render(request, 'enroll/home.html', {'form': fm})
