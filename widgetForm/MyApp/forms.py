

from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class1': 'somecss1', 'id': 'uniqueid', 'size': '40'}))
    name.widget.attrs.update(size='80')
