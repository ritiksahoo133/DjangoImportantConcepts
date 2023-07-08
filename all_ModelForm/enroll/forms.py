from dataclasses import fields
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from enroll.models import Student


class User(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        #exclude = ['name']
