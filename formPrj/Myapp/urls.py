from django.urls import path
from Myapp import views

urlpatterns = [
    path('showData/', views.showFormData)
]
