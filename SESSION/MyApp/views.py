from django.shortcuts import render

# Create your views here.


def set_session(request):
    request.session['name'] = "Ritik"
    request.session['lname'] = "Sahoo"
    return render(request, 'MyApp/setsession.html')


def get_session(request):
    nm = request.session.get('name', default='Guest')
    lnm = request.session.get('lname', default="Guest")
    return render(request, 'MyApp/getsession.html', {'name': nm, 'lname': lnm})


def del_session(request):
    if 'name' in request.session:
        del request.session['name']
        return render(request, 'MyApp/deletesession.html')
    else:
        return render(request, 'MyApp/deletesession.html', {'data': 'session not found'})
