from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', views.home, name='event-home'),
   # path('browse/',views.browse,name='event-browse'),
    path('browse/',PostListView.as_view(),name='event-browse'),
   # path('eventdetail/<int:evt>/',EventDetailView.as_view(),name='eventdetail'),
    path('about/', views.about, name='event-about'),
    path('eventdetail/<int:evt>/', views.eventdetail, name='eventdetail'),
    path('eventdetail/<int:evt>/<str:short>', views.shortlist, name="shortlist")
]