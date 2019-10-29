from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(max_length=500)
    location = forms.CharField(max_length=30)

    #contact = forms.NumberInput()

    class Meta:
        model = User
        fields = ['username','birth_date','email','password1','password2','bio','location']