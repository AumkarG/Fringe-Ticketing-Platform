from django.shortcuts import render
from .models import Event


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'event/home.html', context)


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})

def browse(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request,'event/browse.html',context)

