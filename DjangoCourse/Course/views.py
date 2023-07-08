from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
      return HttpResponse("installed")
def course(request):
      return render(request,'course.html',{'nm':'Django','html':'html'})
