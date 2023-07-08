from django.db import models

# Create your models here.
class Student(models.Model):
      sname=models.CharField(max_length=20)
      gmail=models.CharField(max_length=20)

      class Meta:
            db_table='Student'
      