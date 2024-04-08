from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

class Genre(models.Model):
    type_genre = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.type_genre}"



class Entry(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    likes = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='entries')
    


    
    def excerpt_with_ellipsis(self):
        excerpt_with_ellipsis = self.excerpt
        if len(self.content) > len(self.excerpt):
            excerpt_with_ellipsis += "..."
        return excerpt_with_ellipsis
   

   
        
    def __str__(self):
        return self.title




class Comment (models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name ="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "commenter")
    content = models.TextField(validators=[MaxLengthValidator(500)])
    created_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)  

    def __str__(self):
        return f"Comment {self.content} by {self.author}"









