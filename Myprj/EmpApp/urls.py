
from django.urls import path
from EmpApp import views

urlpatterns = [
    path('test',views.test),
    path('addEmp',views.addEmp),
    path('showAll',views.showAll),
    path('editEmp/<eid>',views.editEmp),
    path('deleteEmp/<eid>',views.deleteEmp)
]