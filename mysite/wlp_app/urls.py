"""
mysite wlp_app
urls.py

Ron Wilton - Started 20/07/2017
"""

from django.conf.urls import url

from wlp_app import views

# each url has been named
urlpatterns = [
	url(r'^$', views.index, name='indexurl'),
	url(r'^photo/(?P<photo_id>[0-9]+)/$', views.photo, name='photourl')
]
