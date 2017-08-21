"""
blog urls.py

Ron Wilton

Started 06/07/2017
"""

from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                 template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                                        template_name = 'blog/post.html'))]
# r'^$'
#   -- leads to the blog's home page
# queryset=Post.objects.all()
#   -- data passed from the database
# "-date"
#   -- order by decending date order
#   -- can order by any column by changing value passed through
# [:25]
#   -- limits the number of blogs to 25
# template_name=
#   -- templates are always looked for at 'templates/'
