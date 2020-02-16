from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static # new

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('myevents/',views.my_events,name='my_events'),
    path('eventlist/',views.event_list,name='list-view'),
    path('deets/<int:pk>',views.evt_detail,name='deets'),
    path('trial/',views.dummy,name='dum')


]