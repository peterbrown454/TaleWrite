from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, f"You are now signed up, {user.username}"
                )
            return redirect('entries:list')
    else:
        form = CreationForm()
    return render(request, "signup.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}")
            next_page = request.POST.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('entries:list')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You are now logged out")
        return redirect("entries:list")
        
    