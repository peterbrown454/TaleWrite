from django.contrib import admin
from .models import Entry, Comment, Genre
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Entry) 
class EntryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status',)
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment) 
class CommentAdmin(SummernoteModelAdmin):

        list_display = ('content', 'author', 'created_on',)
        search_fields = ['author']
        list_filter = ('created_on',)
        prepopulated_fields = {}
        summernote_fields = ('content',)

@admin.register(Genre) 
class GenreAdmin(SummernoteModelAdmin):

    list_display = ('type_genre', 'description',)
    search_fields = ['type_genre']
    list_filter = ('type_genre',)
    prepopulated_fields = {}
    summernote_fields = ('description',)

