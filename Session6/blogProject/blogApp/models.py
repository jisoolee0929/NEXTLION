from turtle import title
from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category_id = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


