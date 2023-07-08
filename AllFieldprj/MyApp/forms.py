
from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=15, strip=False,
                           empty_value="sonam", error_messages={'required': "Enter Your Name"})
