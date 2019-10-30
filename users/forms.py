from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from event.models import Event

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(max_length=500)
    location = forms.CharField(max_length=30)

    #contact = forms.NumberInput()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','birth_date','email','password1','password2','bio','location']
        

class EventCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
       super(EventCreationForm, self).__init__(*args, **kwargs)
       self.fields['date_created'].widget.attrs['readonly'] = True
       self.fields['hoster'].widget.attrs['readonly'] = True

    class Meta:
        model = Event
        fields = ['name','description','location','date_created','hoster','model_pic','verify']
        
       
              
