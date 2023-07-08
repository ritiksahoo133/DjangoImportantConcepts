from django.urls import path
from MyApp import views
urlpatterns = [
    path('student/<int:My_id>', views.showDetails, name="details"),
    path('student/<int:My_id>/<int:sub_id>',
         views.showsubDetails, name="subdetails")
]
