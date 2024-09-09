from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    
