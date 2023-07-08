from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    password2 = forms.CharField(
        label='Enter Password(again)', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class EditUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'last_login', 'date_joined']
        label = {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = "__all__"
