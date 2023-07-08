from django.shortcuts import redirect, render
from django.http import HttpResponse
from deptApp.models import Dept
from datetime import datetime,timedelta
# Create your views here.
def demo(request):
      return HttpResponse('Hello Django')
def addDept(request):
      if(request.method=="GET"):
            return render(request,'addDept.html',{})
      else:
            dname=request.POST["dname"]
            dlocation=request.POST["dlocation"]

            d1=Dept()
            d1.dname=dname
            d1.dlocation=dlocation
            d1.save()
            return redirect(showData)
def showData(request):
      dept=Dept.objects.all()
      return render(request,'showData.html',{"dept":dept})
def cookiesDemo(request):
      if(request.method=="GET"):
            return render(request,'cookiesDemo.html')
      else:
            fname=request.POST['fname']
            lname=request.POST['lname']
            resp=HttpResponse("set cookies")
            resp.set_cookie("fname",fname)
            resp.set_cookie("lname",lname)
            resp.set_cookie('subject','python',expires=datetime.today()+timedelta(days=3))
            return resp

def getCookies(request):
      fname=request.COOKIES['fname']
      lname=request.COOKIES['lname']
      return HttpResponse(fname+" "+lname)
def sessionDemo(request):
      if(request.method=="GET"):
            return render(request,'sessionDemo.html')
      else:
            fname=request.POST['fname']
            lname=request.POST['lname']
            request.session['fname']=fname
            request.session['lname']=lname
            return HttpResponse("session created successfully")


def getSession(request):
      fname=request.session['fname']
      lname=request.session['lname']
      return HttpResponse(fname+" "+lname)


