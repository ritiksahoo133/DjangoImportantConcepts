from django.urls import path
from Course import views

urlpatterns = [
    path('test/',views.test),
    path('crs/',views.course),
]