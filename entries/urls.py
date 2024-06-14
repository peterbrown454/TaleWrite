from django.urls import path, include
from . import views


app_name = 'entries'

urlpatterns = [
    path(
        'entries/like/<slug:slug>/', views.like_entry, name='like_entry'
        ),
    path(
        '', views.entry_list, name="list"
        ),
    path(
        'write', views.entry_write, name="write"
        ),
    path(
        'entries/<slug:slug>/', views.entry_detail, name='entry_detail'
        ),
    path(
        'entries/entries/<slug:slug>/', views.delete_entry, name='delete_entry'
        ),
    path(
        'entries/<pk>/update', views.EditEntry.as_view(), name="EditEntry"
        ),
    path(
        'my_page', views.my_page, name='my_page'
        ),
    path(
        'entry_list_search', views.entry_list_search, name="entry_list_search"
        ),
    path(
        'search_bar_w3', views.search_bar_w3, name='search_bar_w3'
        ),
    path(
        'search_bar_w3_mypage', views.search_bar_w3_mypage, name='search_bar_w3_mypage'
        ),
    path(
        'landing_page', views.landing_page, name='landing_page'
        ),      
]
