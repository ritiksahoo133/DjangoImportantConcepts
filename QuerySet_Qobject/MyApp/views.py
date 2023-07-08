from django.shortcuts import render
from .models import Student, User
from django.db.models import Q


# Create your views here.
# field__lookuptype=value
def StudentView(request):
    stu = Student.objects.filter(Q(id=1) & Q(marks=70))
    stu = Student.objects.filter(Q(id=1) | Q(marks=60))
    return render(request, "MyApp/home.html", {"stu": stu})
