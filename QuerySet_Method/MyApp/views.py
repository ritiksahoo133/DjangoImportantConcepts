from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q


# Create your views here.
def StudentView(request):
    # stu = Student.objects.all()
    # stu = Student.objects.filter(age=22)
    # stu = Student.objects.exclude(age=22)
    # stu = Student.objects.order_by("-marks")
    # stu = Student.objects.order_by("?")
    # stu = Student.objects.order_by("id").reverse()[:3]
    # stu = Student.objects.values("name", "age") #Retrive speccific column
    # stu = Student.objects.values_list("id", "name", named=True)

    # q1 = Student.objects.values_list("id", "name", named=True)
    # q2 = Teacher.objects.values_list("id", "name", named=True)
    # stu = q1.union(q2)

    # q1 = Student.objects.values_list("id", "name", named=True)
    # q2 = Teacher.objects.values_list("id", "name", named=True)
    # stu = q1.union(q2, all=True)

    ############# AND OR Operator ###########
    # stu = Student.objects.filter(id=6) & Student.objects.filter(age=21)
    # stu = Student.objects.filter(id=6, age=21)
    # stu = Student.objects.filter(Q(id=6) & Q(age=21))

    # stu = Student.objects.filter(id=6) | Student.objects.filter(age=21)
    stu = Student.objects.filter(Q(id=6) | Q(age=22))

    print("Return", stu)
    print()
    print(stu.query)
    return render(request, "MyApp/home.html", {"stu": stu})
