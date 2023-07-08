from django.shortcuts import render
from .forms import SignUp
from django.contrib import messages
# Create your views here.


def Sign_Up(request):
    if request.method == 'POST':
        fm = SignUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been signed up')
    else:
        fm = SignUp()
    return render(request, 'Myapp/home.html', {'form': fm})
