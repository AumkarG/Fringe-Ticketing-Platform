from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from event.models import Event
from users.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(max_length=500)
    location = forms.CharField(max_length=30)
    
    #contact = forms.NumberInput()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','birth_date','email','password1','password2','bio','location']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserRegisterForm, self).save(commit=True)
        user_profile = Profile(user=user, birth_date=self.cleaned_data['birth_date'], 
            bio=self.cleaned_data['bio'],location=self.cleaned_data['location'])
        user_profile.save()
        return user, user_profile   

class EventCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
       super(EventCreationForm, self).__init__(*args, **kwargs)
       self.fields['date_created'].widget.attrs['readonly'] = True

    class Meta:
        model = Event
        fields = ['name','description','location','date_created','model_pic','verify']

class UserUpdateForm(ModelForm):
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields=['bio','birth_date','location']