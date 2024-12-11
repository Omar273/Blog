from django.urls import path 
from . import views 

urlpatterns = [ 
       path('', views.hello ),   
       path('index1.html', views.cond1) ,
       path('index2.html', views.cond2)  , 
       path('index3.html', views.cond3)  ]