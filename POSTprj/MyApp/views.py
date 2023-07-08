from django.shortcuts import render
from MyApp.forms import StudentRegistration
# Create your views here.


def showData(request):
    fm = StudentRegistration()
    return render(request, 'MyApp/showData.html', {'form': fm})
