from django.contrib import admin
from .models import Student, User


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "city", "dob", "marks"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "s_name", "email"]
