from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
      return HttpResponse("<h1>Hello Good Morning</h1>")
def hiddenDemo(request):
      if(request.method=="GET"):
            return render(request,'hiddenDemo.html',{})
      else:
            fname=request.POST['fname']
            lname=request.POST['lname']
            uname=fname+""+lname
            return render(request,'hiddenDemo.html',{"uname":uname})