from django.urls import path, include
from . import views

app_name = 'entries'

urlpatterns = [
    path('entries/like/<slug:slug>/', views.like_entry, name='like_entry'),
    path('', views.entry_list, name = "list"),
    path('write', views.entry_write, name = "write"),
    path('entries/<slug:slug>/', views.entry_detail, name='entry_detail'), 
    path('entries/entries/<slug:slug>/',views.delete_entry, name='delete_entry'),
    path('entries/<pk>/update', views.EditEntry.as_view(), name = "EditEntry"),




    
]
