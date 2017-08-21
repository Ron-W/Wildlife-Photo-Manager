"""
mysite
tests.py

Ron Wilton - Started 20/07/2017
"""

from django.test import TestCase

class wlp_appURLsTests(TestCase):
	def test_url_wlp_app_correct_request(self):
		"""
		checks that there is a 'wlp_app' page
		"""
		response = self.client.get('/wlp_app/')
		self.assertEqual(response.status_code, 200)

	def test_url_blog_correct_request(self):
		"""
		checks that there is a 'blog' page
		"""
		response = self.client.get('/blog/')
		self.assertEqual(response.status_code, 200)

	
