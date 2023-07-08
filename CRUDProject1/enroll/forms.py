from dataclasses import fields
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from enroll.models import Student


class User(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
                   'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'text'})}
