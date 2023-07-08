
from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={
                           'required': "Enter Your Name"})
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data['password']
        if(len(password) < 5):
            raise forms.ValidationError("Enter more than 5 value")
        return password

    def clean_name(self):
        name = self.cleaned_data['name']
        if(len(name) < 4):
            raise forms.ValidationError("Enter more than 4 char")
        return name
