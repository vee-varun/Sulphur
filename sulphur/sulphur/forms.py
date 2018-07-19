from django import forms

class signupform(forms.Form):
    genderOptions = [
        (1, 'male'),
        (0, 'female'),
    ]
    username = forms.CharField(label='Username', max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)
    full_name = forms.CharField(label='Full Name', max_length=50)
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect, choices=genderOptions)
    email = forms.EmailField()