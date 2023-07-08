from django.urls import path
from MyApp import views

urlpatterns = [
    path('stuData/', views.showData)
]
