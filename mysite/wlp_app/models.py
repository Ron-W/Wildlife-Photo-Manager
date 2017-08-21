"""
wlp_app
models.py

Ron Wilton - Started 20/07/2017
"""

from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
		

# item in database
class Photo(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	location = models.ForeignKey(Location)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	# The following up loads the photos dependent upon the upload date.
	# This will enable easy seperation of files so that they are not
	# all in the same folder.
	photo_taken = models.ImageField(upload_to='wildlifephotos/%Y/%m/%d',
			null=True, blank=True,
			width_field="width_field", height_field="height_field")

	
	def __str__(self):
		return self.name

		
