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
