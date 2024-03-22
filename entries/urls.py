"""projectjournal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name = 'entries'
from django.urls import path, include
from . import views




urlpatterns = [
    path('entries/like/<slug:slug>/', views.like_entry, name='like_entry'),
    path('', views.entry_list, name = "list"),
    path('write', views.entry_write, name = "write"),
    path('entries/<slug:slug>/', views.entry_detail, name='entry_detail'), 
    #path ('edit/<slug:slug>/', views.entry_update, name ='entry_update'),
    path('entries/entries/<slug:slug>/',views.delete_entry, name='delete_entry'),
    #path('<pk>/update', views.EntryEdit, name = "EntryEdit"),
    path('entries/edit/<slug:slug>/', views.entry_edit, name='entry_edit'),
]
