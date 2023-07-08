from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=False)
    city = models.CharField(max_length=30)
    dob = models.DateField(null=False)
    marks = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=30)
    salary = models.IntegerField(null=False)
    join_date = models.DateField(null=False)

    def __str__(self):
        return self.name
