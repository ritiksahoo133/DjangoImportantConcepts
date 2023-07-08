from django.shortcuts import render
from Myapp.forms import studentRegistration
# Create your views here.


def showData(request):
    fm = studentRegistration()
    return render(request, 'Myapp/showData.html', {'form': fm})
