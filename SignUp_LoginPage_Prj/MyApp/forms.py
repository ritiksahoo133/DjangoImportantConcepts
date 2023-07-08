from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(
        label="ReEnter Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', ]


class UserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'last_login', 'date_joined', 'is_active']
        labels = {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = "__all__"
        exclude = ["password"]
        labels = {"email": "Email"}
