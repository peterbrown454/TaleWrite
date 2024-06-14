from django import forms
from . import models
from .models import Comment


class WriteEntry (forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['slug', 'title', 'genre', 'content', 'excerpt', 'status']


class WriteComment (forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class UpdateEntry (forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['title', 'content', 'excerpt','slug', 'genre',]


