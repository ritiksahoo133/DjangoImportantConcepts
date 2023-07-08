import email
from django.db import models

# Create your models here.
class userinfo(models.Model):
      uname=models.CharField(max_length=20)
      pwd=models.CharField(max_length=20)
      email=models.CharField(max_length=20)

      class Meta:
            db_table='userinfo'