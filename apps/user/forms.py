from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField()
