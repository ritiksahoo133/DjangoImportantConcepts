from django.shortcuts import render
from django.http import HttpResponse
from MyApp.forms import StudentRegistration
# Create your views here.


def test(request):
    return HttpResponse("Hello")


def showData(request):
    fm = StudentRegistration()
    return render(request, 'MyApp/StudentRegistration.html', {'form': fm})
