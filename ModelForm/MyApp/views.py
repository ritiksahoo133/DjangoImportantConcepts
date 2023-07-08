from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Student
from MyApp.forms import User
# Create your views here.


def test(request):
    return render(request, 'MyApp/test.html')


def showData(request):
    if(request.method == "POST"):
        stu = Student.objects.get(pk=9)
        fm = User(request.POST, instance=stu)
        if fm.is_valid():
            #nm = fm.cleaned_data['name']
            #em = fm.cleaned_data['email']
            #pw = fm.cleaned_data['password']
           #stu = Student(name=nm, email=em, password=pw)
            stu.save()
    else:
        fm = User()
    return render(request, 'MyApp/showData.html', {'form': fm})
