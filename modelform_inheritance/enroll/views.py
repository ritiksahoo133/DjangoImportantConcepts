from django.shortcuts import render
from .models import Registration
from .forms import StudentRegistration, TeacherRegistration
# Create your views here.


def test(request):
    return render(request, 'enroll/test.html')


def StudentForm(request):
    if(request.method == 'POST'):
        fm = StudentRegistration(request.POST)
        print(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['student_name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            u = Registration(student_name=nm, email=em, password=pw)
            u.save()
    else:
        fm = StudentRegistration(label_suffix=" ")
    return render(request, 'enroll/student.html', {'form': fm})


def TeacherForm(request):
    if(request.method == 'POST'):
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['teacher_name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            u = Registration(teacher_name=nm, email=em, password=pw)
            u.save()

    else:
        fm = TeacherRegistration()
    return render(request, 'enroll/teacher.html', {'form': fm})
