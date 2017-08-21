"""
mysite
urls.py

Ron Wilton - Started 20/07/2017
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^', include('personal.urls')),
    url(r'^wlp_app/', include('wlp_app.urls')),
	url(r'^blog/', include('blog.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

