from django.db import models

# Create your models here.

class todoPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    detail = models.CharField(max_length=100)
    duedate = models.DateTimeField(null=True)
    left_day = models.BigIntegerField(blank =True)
    def __str__(self):
        return self.title



