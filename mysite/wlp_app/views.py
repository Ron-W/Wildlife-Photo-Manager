"""
wlp_app
views.py

Ron Wilton - Started 20/07/2017
"""

from django.http import HttpResponse
from django.template import loader

from wlp_app.models import Location, Photo


def index(request):
	# get all photo that have 'id' Location
	# Location.objects.get(id=1).item_set.all()

	template = loader.get_template('wlp_app/index.html')
	context = {
		'locations_context' : Location.objects.all(),
		'photos_context' : Photo.objects.all()
	}
	return HttpResponse(template.render(context, request))

	
# URL example.com/photo/1	
def photo(request, photo_id):
	try:
		pht = Photo.objects.get(id=photo_id)
	except Photo.DoesNotExist:
		pht = None
	
	template = loader.get_template('wlp_app/photo.html')
	context = {
		'pht' : pht
	}
	return HttpResponse(template.render(context, request))
	