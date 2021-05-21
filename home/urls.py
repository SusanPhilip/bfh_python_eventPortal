from django.urls import path
from django.urls.resolvers import URLPattern
from .views import  login, signup, userprofile, index, bfh2pageorg,  upcomingorg, Eventgenerator

urlpatterns=[
     path('login/', login, name='login'),
     path('signup/', signup, name='signup'),
     path('userprofile/', userprofile, name='userprofile'),
     path('index/', index, name='index'),
     path('bfh2pageorg', bfh2pageorg, name='bfh2page'),
     path('upcomingorg/',upcomingorg , name='upcomingorg'),
     path('Eventgenerator/',Eventgenerator , name='Eventgenerator'),
]