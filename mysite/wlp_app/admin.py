"""
wlp_app
admin.py

Ron Wilton - Started 20/07/2017
"""

from django.contrib import admin

from wlp_app.models import Location, Photo

admin.site.register(Location)
admin.site.register(Photo)
