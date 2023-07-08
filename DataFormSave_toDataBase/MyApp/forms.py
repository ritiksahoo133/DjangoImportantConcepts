from socket import fromshare
from xml.dom.minidom import Attr
from django import forms


class Student(forms.Form):
    name = forms.CharField(error_messages={'required': "Enter Your Name"})
    email = forms.CharField(error_messages={'required': "Enter Your Email"})
    password = forms.CharField(widget=forms.PasswordInput(),
                               error_messages={
                                   'required': "Enter Your password"})
