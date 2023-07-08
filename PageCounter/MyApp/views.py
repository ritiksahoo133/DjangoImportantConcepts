from django.shortcuts import render

# Create your views here.


def home(request):
    ct = request.session.get('count', 0)
    new_count = ct+1
    request.session['count'] = new_count
    return render(request, 'MyApp/home.html', {'count': new_count})


def login(request):
    if request.method == 'POST':
        return render(request, 'MyApp/login.html', context={'hello': 'hello'})
