from django.shortcuts import render
from .models import Student, User
from django.db.models import Sum, Min, Avg, Max, Count


# Create your views here.
# field__lookuptype=value
def StudentView(request):
    stu = Student.objects.all()
    sum_marks = stu.aggregate(Sum("marks"))
    Avg_marks = stu.aggregate(Avg("marks"))
    Min_marks = stu.aggregate(Min("marks"))
    print("student", stu)
    print("sum", sum_marks)
    print("Avg", Avg_marks)
    print("Min_marks", Min_marks)
    print("Return", stu.query)
    return render(request, "MyApp/home.html", {"stu": stu})
