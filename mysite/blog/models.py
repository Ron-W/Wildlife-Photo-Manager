"""
blog models.py

Ron Wilton

Started 06/07/2017
"""

from django.db import models

class Post(models.Model):
    # defining columns in table
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

