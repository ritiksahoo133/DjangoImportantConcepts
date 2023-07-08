from django.contrib import admin
from .models import Student, Teacher


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "city", "dob", "marks"]


@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "empnum", "city", "salary", "join_date"]
