from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Page(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
