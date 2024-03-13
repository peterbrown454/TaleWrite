from django.shortcuts import render
from . import views
from django.urls import path, include


app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup_view, name = "signup")
    
   
]