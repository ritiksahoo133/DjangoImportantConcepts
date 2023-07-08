from django.contrib import admin
from MyApp.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


admin.site.register(User, UserAdmin)
