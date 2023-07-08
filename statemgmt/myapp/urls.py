from django.urls import path
from myapp import views

urlpatterns = [
    path('test',views.test),
    path('hiddenDemo',views.hiddenDemo),
]