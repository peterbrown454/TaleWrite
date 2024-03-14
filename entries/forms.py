from django import forms
from . import models

class WriteEntry (forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['title', 'content', 'excerpt','slug', 'thumb']
