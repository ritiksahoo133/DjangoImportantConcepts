from django.shortcuts import render
from .models import User, Post
from django.http import HttpResponse


# Create your views here.
def home(request):
    user = User.objects.all()
    for u in user:
        print(u.id, u.username)
    user = User.objects.get(username=request.user.username)
    print("---", user.username)
    post = Post.objects.filter(user=request.user)
    print("------------------------")
    for p in post:
        print(p.id, " ", p.user, " ", p.city, " ", p.age)

    print("--------user-----------")
    user = User.objects.get(username=request.user)
    print(user.id, user.username)
    post = Post.objects.filter(user=request.user)
    print("----------------------")
    for p in post:
        print(p.user, p.city, p.age)
    return HttpResponse("Run successfully")
