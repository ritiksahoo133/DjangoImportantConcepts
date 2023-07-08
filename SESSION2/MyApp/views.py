from django.shortcuts import render

# Create your views here.


def set_session(request):
    request.session['name'] = "Ritik"
    request.session['lname'] = "Sahoo"
    return render(request, 'MyApp/setsession.html')


def get_session(request):
    nm = request.session.get('name', default='Guest')
    lnm = request.session.get('lname', default="Guest")
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'MyApp/getsession.html', {'name': nm, 'lname': lnm, 'keys': keys, 'items': items})


def del_session(request):
    request.session.flush()
    return render(request, 'MyApp/deletesession.html')
