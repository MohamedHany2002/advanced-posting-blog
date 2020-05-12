from django import forms


class email_form(forms.Form):
    email=forms.EmailField()