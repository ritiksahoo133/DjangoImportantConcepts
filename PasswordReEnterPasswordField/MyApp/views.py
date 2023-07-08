from django.shortcuts import render
from MyApp.forms import PasswordGenerate
# Create your views here.


def Password(request):
    if(request.method == "POST"):
        fm = PasswordGenerate(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            Password = fm.cleaned_data['password']
            repassword = fm.cleaned_data['repassword']
            print('password:', Password)
            print('repassword:', repassword)

    else:
        fm = PasswordGenerate()
    return render(request, 'MyApp/PasswordGenerate.html', {'form': fm})
