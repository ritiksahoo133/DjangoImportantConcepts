from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupList.as_view()),
    path('signup_details/<id>', views.SignupDetails.as_view()),
]
