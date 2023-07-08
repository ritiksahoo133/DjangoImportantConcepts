from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import User
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        fm = User(request.POST, label_suffix="")
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            stu = Student(name=nm, email=em, password=pw)
            stu.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Now You Can Login")
            #messages.debug(request, "This is debug messages")
            #messages.info(request, "This is info messages")
            #messages.warning(request, "This is Warning message")
            #messages.error(request, "This error message")
            print(messages.get_level(request))
            messages.debug(request, "This is debug messages")
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, "This is New debug messages")
            print(messages.get_level(request))
            messages.error(request, "This is error")
    else:
        fm = User()
    return render(request, 'enroll/test.html', {'form': fm})
