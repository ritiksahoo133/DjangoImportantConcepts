from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
      return HttpResponse("Hello")
def setmgmt(request):
      if(request.method=="GET"):
            return render(request,'setmgmt.html',{})
      else:
            sname=request.POST['sname']
            gmail=request.POST['gmail']
            resp=HttpResponse("set Cookies")
            resp.set_cookie('sname',sname)
            resp.set_cookie('gmail',gmail)
            return resp
def getCookies(request):
      sname=request.COOKIES['sname']
      gmail=request.COOKIES['gmail']
      return HttpResponse("sname="+sname+" "+"gmail="+gmail)

def setSession(request):
      if(request.method=="GET"):
            return render(request,'session.html')
      else:
            fname=request.POST['fname']
            lname=request.POST['lname']
            request.session['fname']=fname
            request.session['lname']=lname
            return HttpResponse("Added successfully")
def getSession(request):
      fname=request.session['fname']
      lname=request.session['lname']
      return HttpResponse(fname+" "+lname)