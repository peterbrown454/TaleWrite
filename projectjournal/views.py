from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about (request):
    #return HttpResponse ("this is the about page")
    return render (request, 'about.html')

def home (request):
    #return HttpResponse ("this is the home page")
    return render (request, 'homepage.html')

