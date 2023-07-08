from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def set_session(request):
    request.session['name'] = "Ritik"
    request.session['lname'] = "Sahoo"
    print(request.session.get_expiry_age())
    return render(request, 'MyApp/setsession.html')


def get_session(request):
    if 'name' in request.session:
        nm = request.session.get('name', default='Guest')
        lnm = request.session.get('lname', default="Guest")
        request.session.modified = True
        return render(request, 'MyApp/getsession.html', {'name': nm, 'lname': lnm})
    else:
        return HttpResponse("Your Session has expired")


def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'MyApp/deletesession.html')
