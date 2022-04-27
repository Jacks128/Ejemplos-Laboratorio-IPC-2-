from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    remember = forms.BooleanField(label="exampleCheck1", required=False)

class FileForm(forms.Form):
    file=forms.FileField(label="file")

class AddForm(forms.Form):
   name = forms.CharField(label="name")
   artist = forms.CharField(label="artist")
   image = forms.CharField(label="image")
   album = forms.CharField(label="album") 