from django.shortcuts import render
from Myapp.forms import StudentRegistration
# Create your views here.


def showFormData(request):
    fm = StudentRegistration(
        label_suffix=" ",)

    return render(request, 'Myapp/name.html', {'form': fm})
