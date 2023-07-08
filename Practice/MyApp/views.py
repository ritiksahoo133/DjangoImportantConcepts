from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.
def StudentView(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")
