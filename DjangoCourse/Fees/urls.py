from django.urls import path
from Fees import views

urlpatterns = [
    path('test/',views.test),
]