from django.shortcuts import render
from MyApp.forms import StudentRegistration
# Create your views here.


def showData(request):
    if(request.method == "POST"):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name:', name)
    else:
        fm = StudentRegistration()
    return render(request, 'MyApp/StudentRegistration.html', {'form': fm})
