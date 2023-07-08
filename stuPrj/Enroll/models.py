from django.db import models


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stumail = models.EmailField(max_length=50)
    stuage = models.IntegerField()

    def __str__(self):
        return self.stuname
