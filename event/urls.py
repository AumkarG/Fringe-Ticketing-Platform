from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('browse/',views.browse,name='event-browse'),
    path('about/', views.about, name='event-about'),
    path('eventdetail/', views.eventdetail, name='eventdetail'),
]