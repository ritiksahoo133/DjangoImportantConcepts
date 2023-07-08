from django.contrib import admin
from .models import Registration
# Register your models here.


@admin.register(Registration)
class ModelRegistration(admin.ModelAdmin):
    list_display = ['student_name', 'teacher_name', 'email', 'password']
