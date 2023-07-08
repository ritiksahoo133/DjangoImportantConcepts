from django import forms


class PasswordGenerate(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter Your Name'})
    email = forms.CharField(error_messages={'required': 'Enter Your Email'})
    password = forms.CharField(widget=forms.PasswordInput())
    repassword = forms.CharField(
        label="Re-Enter Password", widget=forms.PasswordInput())

    def clean(self):
        #cleaned_data = super().clean()
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']

        if(password != repassword):
            raise forms.ValidationError("password doesn't match")
