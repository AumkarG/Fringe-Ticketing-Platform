from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import EventCreationForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please try to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')

def create(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('my_events')
    else:
        form =  EventCreationForm(initial={'hoster': request.user})
    return render(request, 'users/create.html', {'form': form})

def my_events(request):
    return render(request,'users/myevents.html')

