from django.db import models

# Create your models here.
class Entry (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    

    #add in thumbnail
    #add in author