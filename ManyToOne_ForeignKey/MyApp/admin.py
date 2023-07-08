from django.contrib import admin
from MyApp.models import Post


# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["id", "user", "city", "age"]
