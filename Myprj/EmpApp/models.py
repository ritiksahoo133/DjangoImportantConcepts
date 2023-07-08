from django.db import models
from requests import request

# Create your models here.
class Emp(models.Model):
      Ename=models.CharField(max_length=20)
      salary=models.CharField(max_length=20)
      location=models.CharField(max_length=20)

      class Meta:
            db_table='Emp'