from django.urls import path
from medicine import views
urlpatterns = [
    path('signup/', views.UserSignup, name="signup"),
    path('login/', views.UserLogin, name="Login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.Logout, name='logout'),
    path('changepassword/', views.changePassword, name='changepassword'),
    path('userdetails/<int:id>', views.userdetails, name="userdetails"),
]
