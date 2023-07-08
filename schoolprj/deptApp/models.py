from django.db import models

# Create your models here.
class Dept(models.Model):
      dname=models.CharField(max_length=20)
      dlocation=models.CharField(max_length=20)

      class Meta:
            db_table="Dept"
