from django import forms


class studentRegistration(forms.Form):
    name = forms.CharField(
        label="Enter Name", label_suffix="", initial="Ritik", required=False, disabled=False, help_text="Limit 70 Char",)
