from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    remember = forms.BooleanField(label="exampleCheck1", required=False)