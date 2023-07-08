from django.shortcuts import render

# Create your views here.


def set_cookies(request):
    response = render(request, 'MyApp/setcookies.html')
    response.set_cookie('name', 'Ritik', max_age=50000)
    return response


def get_cookies(request):
    nm = request.COOKIES.get('name', 'Guest')
    return render(request, 'MyApp/getcookies.html', {'nm': nm})


def delete_cookies(request):
    response = render(request, 'MyApp/setcookies.html')
    response.delete_cookie('name')
    return response
