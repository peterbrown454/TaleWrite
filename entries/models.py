from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
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
    status = models.IntegerField(choices=STATUS, default=0)

    
    def excerpt_with_ellipsis(self):
        excerpt_with_ellipsis = self.excerpt
        if len(self.content) > len(self.excerpt):
            excerpt_with_ellipsis += "..."
        return excerpt_with_ellipsis
   

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return self.title




class Comment (models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name ="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "commenter")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)  
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Comment {self.content} by {self.author}"



