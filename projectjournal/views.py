from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about (request):
    return HttpResponse ("this is the about page")

def home_view (request):
    return HttpResponse ("this is the home page")