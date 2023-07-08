from django.contrib import admin
from .models import signup
# Register your models here.


class SignupAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']


admin.site.register(signup, SignupAdmin)
