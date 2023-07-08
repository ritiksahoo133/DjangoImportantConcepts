from django.urls import path
from LoginApp import views
urlpatterns = [
    path('test',views.test),
    path('signup',views.signup),
    path('Login',views.Login),
]