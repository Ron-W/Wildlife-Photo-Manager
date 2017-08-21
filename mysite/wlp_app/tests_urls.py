"""
mysite
tests_urls.py

Ron Wilton - Started 20/07/2017
"""

from django.test import TestCase
from wlp_app.models import Photo

class wlp_appURLsTests(TestCase):
	def test_url_photo_page_is_found(self):
		"""
		the user requests a correct photo url
		"""
		# need to ensure that 'photo_id' actually exists
		response = self.client.get('wlp_app/photo/')
		self.assertEqual(response.status_code, 200)

	def test_url_photo_page_incorrect(self):
		"""
		the user requests an incorrect photo url
		"""
		response = self.client.get('photo/abc')
		self.assertEqual(response.status_code, 404)
	
