"""
mysite
tests_views.py

Ron Wilton - Started 28/07/2017
"""

from django.test import TestCase
from django.urls import reverse

#from .models import Location
from wlp_app.models import Location, Photo

# should this function be in another file from which it can be tested??
def create_location(location_text):
	"""
	creates a location
	"""
	return Location.objects.create(name=location_text)

def create_photo(photo_text, desc, loca):
	"""
	creates a photo
	"""
	return Photo.objects.create(name=photo_text, description=desc, location=loca)

class PhotosByLocationIndexViewTests(TestCase):
	"""
	testing 'def photo(requeset)'
	number for 'photo_id' does not exist
	"""
	def test_for_invalid_photo_ID_number(self):
		# 'photourl' is in 'wlp_app/urls.py'
		response = self.client.get(reverse('photourl', kwargs={'photo_id':0}))
		self.assertEqual(response.status_code, 200)
		# '"Invalid item ID"' is in 'wlp_app/photos.html'
		self.assertContains(response, "Invalid photo ID")

	"""
	testing 'def photo(request)'
	correct 'photo_id'
	"""
	def test_for_correct_photo_ID_number(self):
		# create a photo
		#create_location("This is not a location")
		the_name = "A mushroom"
		the_desc = "Can be poisonous"
		loca_id = create_location("This is not a location")
		create_photo(the_name, the_desc, loca_id)
		# 'photourl' is in 'wlp_app/urls.py'
		response = self.client.get(reverse('photourl', kwargs={'photo_id':1}))
		self.assertEqual(response.status_code, 200)
		# can the names be read back??
		self.assertContains(response, the_name)
		self.assertContains(response, the_desc)
		self.assertEqual(response, loca_id)
		
		
		

	"""
	testing 'def photo(requeset)'
	'photo_id' is not numeric
	"""
	"""
	def test_for_incorrect_photo_ID_number(self):
		# 'photourl' is in 'wlp_app/urls.py'
		both the following two lines give the following error message during testing
		django.urls.exceptions.NoReverseMatch: Reverse for 'photourl' with keyword arguments '{'photo_id': 'abc'}' not found. 1 pattern(s) tried: ['wlp_app/photo/(?P<photo_id>[0-9]+)/$']
		assuming that it is not possible to test for '127.0.0.1:8000/wlp_app/photo/abc/' using this method
		response = self.client.get(reverse('photourl', kwargs={'photo_id':abc}))
		response = self.client.get(reverse('photourl', kwargs={'photo_id':'abc'}))
		self.assertEqual(response.status_code, 404)
	"""
		

	"""
	testing 'def index(requeset)'
	"""
	def test_for_no_locations(self):
		"""
		if there are no locations, then a suitable message is shown
		"""
		# 'indexurl' is in 'wlp_app/urls.py'
		response = self.client.get(reverse('indexurl'))
		self.assertEqual(response.status_code, 200)
		# '"There are no locations."' is in 'wlp_app/index.html'
		self.assertContains(response, "There are no locations.")
		# 'locations_context' is in 'def index(request) in 'views.py'
		self.assertQuerysetEqual(response.context['locations_context'], [])


	def test_for_no_photos_in_index(self):
		"""
		if there are no photos, then a suitable message is shown
		NOTE: one location needs to be created
		"""
		# create a location
		create_location("This is not a location")
		# 'indexurl' is in 'wlp_app/urls.py'
		# 'self.client.get' returns a Response object
		response = self.client.get(reverse('indexurl'))
		self.assertEqual(response.status_code, 200)
		# '"There are no photos available."' is in 'wlp_app/index.html'
		self.assertContains(response, "There are no photos available.")
		
		# 'photos_context' is in 'def index(request) in 'views.py'
		self.assertQuerysetEqual(response.context['photos_context'], [])
		
