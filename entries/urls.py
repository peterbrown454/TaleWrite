from django.urls import path, include
from . import views
from .views import search_bar

app_name = 'entries'

urlpatterns = [
    path('entries/like/<slug:slug>/', views.like_entry, name='like_entry'),
    # path('', views.entry_list, name = "list"),
    path('', views.EntryListView.as_view(), name = "list"),
    path('write', views.entry_write, name = "write"),
    path('entries/<slug:slug>/', views.entry_detail, name='entry_detail'), 
    path('entries/entries/<slug:slug>/',views.delete_entry, name='delete_entry'),
    path('entries/<pk>/update', views.EditEntry.as_view(), name = "EditEntry"),
    path('entry_list_draft', views.entry_list_draft, name = "entry_list_draft"),
    # path('entry_list_genre', views.entry_list_genre, name = "entry_list_genre"),
    path('entry_list_search', views.entry_list_search, name = "entry_list_search"),
    path('search_bar', views.search_bar.as_view(), name = 'search_bar'),
    path('two', views.two.as_view(), name = "two"),
    path('search_bar_w3', views.search_bar_w3, name = 'search_bar_w3'),
    




    
]
