"""
mysite
tests_apps.py

Ron Wilton - Started 28/07/2017
"""

from django.test import TestCase
from wlp_app.apps import WlpAppConfig

class wlp_appAppsTests(TestCase):
	def test_WlpAppConfig(self):
		"""
		ensures that 'WlpAppConfig(AppConfig)' returns the
		correct name
		"""
		self.assertEqual(WlpAppConfig.name, 'wlp_app')
	
