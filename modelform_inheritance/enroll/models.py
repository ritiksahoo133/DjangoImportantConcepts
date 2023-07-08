from django.db import models

# Create your models here.


class Registration(models.Model):
    student_name = models.CharField(max_length=30)
    teacher_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
