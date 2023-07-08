from django.urls import path
from enroll import views
urlpatterns = [
    path('updatestudent/', views.updatestudent, name="updatestudent"),
]
