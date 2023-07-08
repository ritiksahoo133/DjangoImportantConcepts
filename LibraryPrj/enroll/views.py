from django.shortcuts import render
from enroll.forms import LoginForm
# Create your views here.


def showformdata(request):
    fm = LoginForm(auto_id="user_%s", label_suffix=' ',
                   initial={'name': 'Ritik', 'email': 'ritiksahoo133@gmail.com'})
    fm.order_fields(field_order=['email', 'name'])
    return render(request, 'enroll/LoginForm.html', {'form': fm})
