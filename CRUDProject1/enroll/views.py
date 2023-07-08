from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import User
from .models import Student
# Create your views here.


def home(request):
    return render(request, 'enroll/base.html')


def deleteData(request, id):
    d1 = Student.objects.get(pk=id)
    d1.delete()
    return redirect(addnshow)


def addnshow(request):
    if request.method == "POST":
        fm = User(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            u1 = Student(name=nm, email=em, password=pw)
            u1.save()
            fm = User()
    else:
        fm = User()
    stu = Student.objects.all()
    print(stu)
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stud': stu})


def updateStudent(request, id):
    if(request.method == 'POST'):
        stu = Student.objects.get(pk=id)
        fm = User(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
    else:
        stu = Student.objects.get(pk=id)
        fm = User(instance=stu)
    return render(request, 'enroll/updatestudent.html', {'form': fm})
