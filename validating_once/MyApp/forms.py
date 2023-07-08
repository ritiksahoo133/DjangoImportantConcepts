from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={
                           'required': "Enter Your Name"}, min_length=5, max_length=15)
    email = forms.EmailField(error_messages={
        'required': "Enter Your Email"}, min_length=5, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={
        'required': "Enter password"})
