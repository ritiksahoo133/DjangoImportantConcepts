from django.shortcuts import render
from .models import Student


# Create your views here.
def studentView(request):
    # stu = Student.objects.all()
    # stu, created = Student.objects.get_or_create(
    #   name="Rakul", age="21", city="sambalpur", dob="2023-5-24", marks="23"
    # )
    # print(created)
    # stu = Student.objects.order_by("name").first()
    # stu = Student.objects.get(id=1)
    # print(Student.objects.filter(id=stu.id).exists())
    stu = Student.objects.filter(city="sambalpur").update(marks="90")
    return render(request, "MyApp/home.html", {"stu": stu})
