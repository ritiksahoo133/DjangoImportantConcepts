from django.urls import path
from MyApp import views
urlpatterns = [
    path('Login/', views.stuLogin),
    path('success/', views.thanks)
]
