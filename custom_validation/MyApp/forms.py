
from signal import raise_signal
from django import forms
from django.core import validators


def number(value):
    number = str(value)
    if(len(number) != 11):
        raise forms.ValidationError("Mobile Number Should 10 digit")
    return number


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    number = forms.IntegerField()

    def validate_number(self, value):
        number = int(value)
        if(number != 10):
            raise forms.ValidationError("Mobile number must be 10 digit")
