"""
blog admin.py

Ron Wilton

Started 06/07/2017
"""

from django.contrib import admin
# defines table created for the blogs
from blog.models import Post

# Register your models here.
admin.site.register(Post)
