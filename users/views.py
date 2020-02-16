from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import EventCreationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,DetailView,CreateView
from django.http import JsonResponse
from event.models import Event
import json
import requests  
from django.http import StreamingHttpResponse

def event_list(request):
   MAX_OBJECTS = 5
   evts = Event.objects.all()[:MAX_OBJECTS]
   data = {"results": list(evts.values("name", "description", "hoster","location"))}
   return JsonResponse(data)


def evt_detail(request, pk):
   e=Event.objects.get(id=pk)
   data = {"results": {"question": e.name,"pub_date": e.location }}
   return JsonResponse(data)


def dummy(request):
  if request.method=='POST':
            received_json_data=json.loads(request.POST['data'])
            #received_json_data=json.loads(request.body)
            return StreamingHttpResponse('it was post request: '+str(received_json_data))



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
   if request.user.is_authenticated: 
     if request.method=='POST':
       u_form=UserUpdateForm(request.POST,instance=request.user)
       p_form=ProfileUpdateForm(request.POST,instance=request.user.profile)
       if(u_form.is_valid and p_form.is_valid):
           u_form.save()
           p_form.save()
           messages.success(request,f'Your account has been updated')
           return redirect('profile')
     else:
       u_form=UserUpdateForm(instance=request.user)
       p_form=ProfileUpdateForm(instance=request.user.profile) 
     context={
          'u_form':u_form,
          'p_form':p_form
       }
     return render(request, 'users/profile.html',context)
   else:
       messages.info(request, 'Please login to view your profile')
       return redirect('login')

def create(request):
   if request.user.is_authenticated: 
    if request.method == 'POST':
        form = EventCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.hoster=request.user
            form.save()
        return redirect('event-browse')
    else:
        form =  EventCreationForm()
    return render(request, 'users/create.html', {'form': form})
   else:
       messages.info(request, 'Please login to upload an event!')
       return redirect('login')

class EventCreateView(CreateView):
  model=Event
  fields = ['name','description','location','date_created','hoster','model_pic','verify']


def my_events(request):
   if request.user.is_authenticated: 
     return render(request,'users/myevents.html')
   else:
     messages.info(request, 'Please login to view your event!')
     return redirect('login')

