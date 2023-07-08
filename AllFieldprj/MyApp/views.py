from django.shortcuts import render
from MyApp.forms import StudentRegistration
# Create your views here.


def showData(request):
    if(request.method == "POST"):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            print("Name:", name, sep=" ")
            print('----POST----')
    else:
        fm = StudentRegistration()
        print("-----GET-----")
    return render(request, 'MyApp/showData.html', {'form': fm})
