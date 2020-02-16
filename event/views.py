from django.shortcuts import render
from .models import Event
from django.views.generic import ListView,DetailView

def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'event/home.html', context)


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})



#def browse(request):
#    context = {
#        'events': Event.objects.all(),
#    }
#    return render(request,'event/browse.html',context)

class PostListView(ListView):
    model=Event
    template_name='event/browse.html'
    context_object_name='events'
    ordering=['-date_created']



def eventdetail(request,evt):
    e=Event.objects.get(id=evt)
    short=request.user.profile.shortlisted.all()
    
    context = {
        'event': e,
        'short':short
    }
    return render(request,'event/eventdetail.html',context)


def shortlist(request,evt,short):
    e=Event.objects.get(id=evt)
    if(short=='s'):
       request.user.profile.shortlisted.add(e)
    elif (short=='n'):
       request.user.profile.shortlisted.remove(e)
    return eventdetail(request,e.id)

