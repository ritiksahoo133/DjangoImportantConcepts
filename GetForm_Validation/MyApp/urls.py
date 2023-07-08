from django.urls import path
from MyApp import views
urlpatterns = [
    path('test/', views.test,),
    path('showData/', views.showData)
]
