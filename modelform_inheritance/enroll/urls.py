from django.urls import path
from enroll import views

urlpatterns = [
    path('student/', views.StudentForm),
    path('teacher/', views.TeacherForm)
]
