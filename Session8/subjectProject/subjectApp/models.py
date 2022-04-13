from django.db import models

import subjectApp

# Create your models here.


class Major(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    major = models.ForeignKey(
        "Major", on_delete=models.CASCADE, related_name='subjects')
    subject_name = models.CharField(max_length=255, blank=True, null=True)
    prof_name = models.CharField(max_length=255, blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return str(self.subject_name)

