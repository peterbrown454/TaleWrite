from django import forms
from . import models

class WriteEntry (forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['title', 'content', 'excerpt','slug', 'thumb']

    widgets = {
        'content': forms.Textarea(attrs={'rows': 40, 'cols': 2}),  # Adjust rows and cols as needed
    }
