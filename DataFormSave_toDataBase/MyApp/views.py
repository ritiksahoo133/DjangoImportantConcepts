import email
from urllib import request
from django.shortcuts import render
from MyApp.forms import Student
from MyApp.models import User
# Create your views here.


def showData(request):
    if(request.method == "POST"):
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print('name', nm)
            print('Email', em)
            print('password', pw)
            stu = User()
            stu.name = nm
            stu.email = em
            stu.save()

    else:
        fm = Student()
    return render(request, 'MyApp/showData.html', {'form': fm})
