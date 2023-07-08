
from django.urls import path
from . import views
urlpatterns = [
    path('demo/',views.demo),
    path('addDept',views.addDept),
    path('showData',views.showData),
    path('cookiesDemo',views.cookiesDemo),
    path('getCookies',views.getCookies),
    path('sessionDemo',views.sessionDemo),
    path('getSession',views.getSession),
]