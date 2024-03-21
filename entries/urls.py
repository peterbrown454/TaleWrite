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
    path('like/<int:entry_id>/', views.like_entry, name='like_entry'),
    path('', views.entry_list, name = "list"),
    path('write', views.entry_write, name = "write"),
    path('entries/<slug:slug>/', views.entry_detail, name='entry_detail'),
    #path('entry/edit/<slug:slug>/', views.edit_entry_view.as_view(), name='edit_entry_view'),
    #path ('edit/<slug:slug>/', views.entry_update, name ='entry_update'),
    path('entries/entries/<slug:slug>/',views.delete_entry, name='delete_entry'),
    #path('<pk>/update', views.EntryEdit, name = "EntryEdit"),
]
