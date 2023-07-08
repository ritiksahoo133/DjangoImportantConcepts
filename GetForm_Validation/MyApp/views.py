
from django.shortcuts import render
from MyApp.forms import StudentRegistration
from django.http import HttpResponse
# Create your views here.


def test(request):
    return HttpResponse("Hello")


def showData(request):
    if(request.method == "POST"):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']

            print("Name:", name)
            print("Email:", email)
            print('----POST----')
    else:
        fm = StudentRegistration()
        print("-----GET-----")
    return render(request, 'MyApp/showData.html', {'form': fm})
