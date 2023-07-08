from django.db import models

# Create your models here.


class signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "signup"
