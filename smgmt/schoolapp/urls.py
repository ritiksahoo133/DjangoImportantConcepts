from django.urls import path
from schoolapp import views

urlpatterns = [
    path('test',views.test),
    path('setmgmt',views.setmgmt),
    path('getmgmt',views.getCookies),
    path('setSession',views.setSession),
    path('getSession',views.getSession),
]