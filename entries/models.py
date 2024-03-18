from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    thumb = models.ImageField(default="default.png", blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None) 
    likes = models.IntegerField(default=0) 
    genre = models.CharField(max_length=20, null=True)

    
    def excerpt_with_ellipsis(self):
        excerpt_with_ellipsis = self.excerpt
        if len(self.content) > len(self.excerpt):
            excerpt_with_ellipsis += "..."
        return excerpt_with_ellipsis
   

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return self.title



 


 

    #add in thumbnail
    #add in author