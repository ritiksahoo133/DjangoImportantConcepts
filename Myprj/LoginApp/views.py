from django.shortcuts import redirect, render
from django.http import HttpResponse
from LoginApp.models import userinfo
# Create your views here.
def test(request):
      return HttpResponse('Hello Django')
def signup(request):
      if(request.method=="GET"):
            return render(request,'signup.html',{})
      else:
            uname=request.POST['uname']
            pwd=request.POST['pwd']
            email=request.POST['email']
            u1=userinfo()
            u1.uname=uname
            u1.pwd=pwd
            u1.email=email
            u1.save()
            return redirect(Login)
def Login(request):
      if(request.method=="GET"):
            return render(request,'Login.html',{})
      else:
            uname=request.POST['uname']
            pwd=request.POST['pwd']
            try:
                  u1=userinfo.objects.get(uname=uname,pwd=pwd)
                  return HttpResponse("Login successful")
            except:
                  return HttpResponse("Login Failed")

      