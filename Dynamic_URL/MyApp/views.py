from django.shortcuts import render

# Create your views here.


def home(request, check):
    return render(request, 'MyApp/home.html', {'check': check})


def showDetails(request, My_id):
    if(My_id == 1):
        student = {'id': My_id, 'name': 'Rohan'}
    if(My_id == 2):
        student = {'id': My_id, 'name': 'Ritik'}
    if(My_id == 3):
        student = {'id': My_id, 'name': 'Rakesh'}
    return render(request, 'MyApp/showDetails.html', student)


def showsubDetails(request, My_id, sub_id):
    if(My_id == 1 and sub_id == 5):
        student = {'id': My_id, 'name': 'Rohan'}
    if(My_id == 2 and sub_id == 10):
        student = {'id': My_id, 'name': 'Ritik'}
    if(My_id == 3 and sub_id == 15):
        student = {'id': My_id, 'name': 'Rakesh'}
    return render(request, 'MyApp/showDetails.html', student)
