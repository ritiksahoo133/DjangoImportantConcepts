from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import Student
from django.core import validators


class User(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Name',
                  'email': 'Enter Email', 'password': 'Enter password'}
        help_text = {'name': 'Enter Your Full Name'}
        error_messages = {'name': {'required': 'Enter Your Name'},
                          'email': {'required': 'Enter Your Email'},
                          'password': {'required': 'Enter Your Password'}}
        widget = {'password': forms.PasswordInput()}
