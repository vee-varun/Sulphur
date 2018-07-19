from django import forms

class loginform(forms.Form):
    username = forms.CharField(label='Username', max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)