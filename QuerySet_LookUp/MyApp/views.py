from django.shortcuts import render
from .models import Student, User


# Create your views here.
# field__lookuptype=value
def StudentView(request):
    # stu = Student.objects.filter(name__startswith="R")
    # stu = Student.objects.filter(city__exact="sambalpur")
    # stu = Student.objects.filter(city__iexact="sambalpur")
    # stu = Student.objects.filter(name__contains="s")
    # stu = Student.objects.filter(city__icontains="am")
    # stu = Student.objects.filter(id__in=[1, 2])
    # stu = Student.objects.filter(marks__in=[90, 70])
    # stu = Student.objects.filter(marks__gt=70)
    # stu = Student.objects.filter(marks__gte=70)
    # stu = Student.objects.filter(marks__lt=70)
    # stu = Student.objects.filter(marks__lte=70)
    # stu = Student.objects.filter(dob__range=("1976-05-09", "2023-05-24"))
    # stu = Student.objects.filter(dob__year__gte="2001")
    stu = Student.objects.filter(dob__year__gte="2001").filter(marks=70)
    print(stu)
    print()
    print("Return", stu.query)
    return render(request, "MyApp/home.html", {"stu": stu})
