from django.shortcuts import render
from MyApp.forms import Login
from django.http import HttpResponseRedirect
# Create your views here.


def thanks(request):
    return render(request, 'MyApp/success.html')


def stuLogin(request):
    if(request.method == "POST"):
        fm = Login(request.POST)
        if fm.is_valid():
            print("validate")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            return HttpResponseRedirect('MyApp/success/')
    else:
        print("GET")
        fm = Login()
    return render(request, 'MyApp/stuLogin.html', {'form': fm})
