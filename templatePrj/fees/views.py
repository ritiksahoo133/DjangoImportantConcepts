from django.shortcuts import render

# Create your views here.
def feesdetails(request):
      return render(request,'fees/feesdetails.html')