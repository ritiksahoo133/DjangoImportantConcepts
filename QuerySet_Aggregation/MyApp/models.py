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


class User(models.Model):
    s_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.s_name)
