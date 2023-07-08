
from django.shortcuts import redirect, render
from django.http import HttpResponse
from EmpApp.models import Emp
# Create your views here.
def test(request):
      return HttpResponse('Django')
def addEmp(request):
      if(request.method=="GET"):
            return render(request,'addEmp.html',{})
      else:
            emp=Emp()
            emp.Ename=request.POST['Ename']
            emp.salary=request.POST['salary']
            emp.location=request.POST['location']
            emp.save()
            return redirect(showAll)
def showAll(request):
      emp=Emp.objects.all()
      return render(request,'showAll.html',{"emp":emp})
def editEmp(request,eid):
      emp=Emp.objects.get(id=eid)
      if(request.method=="GET"):
            return render(request,'editEmp.html',{"emp":emp})
      else:
            emp.Ename=request.POST['Ename']
            emp.salary=request.POST['salary']
            emp.location=request.POST['location']
            emp.save()
            return redirect(showAll)
def deleteEmp(request,eid):
      emp=Emp.objects.get(id=eid)
      if(request.method=="GET"):
            return render(request,'deleteEmp.html',{})
      else:
            action=request.POST['action']
            if(action=="yes"):
                  emp.delete()
            return redirect(showAll)
