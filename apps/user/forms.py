from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11, min_length=11)


class SignUpForm(forms.Form):
    phone = forms.CharField(max_length=11, min_length=11)
    name = forms.CharField(max_length=64)
    family_name = forms.CharField(max_length=64, required=False)
    code = forms.CharField(max_length=6, min_length=6)
    profile_image = forms.FileField(required=False)


class ActivationForm(forms.Form):
    phone = forms.CharField(max_length=11, min_length=11)
    code = forms.CharField(max_length=6, min_length=6)

