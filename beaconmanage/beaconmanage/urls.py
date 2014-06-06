from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^beacon/', include('beacon.urls', namespace='beacons', app_name='beacon')),
    url(r'^admin/', include(admin.site.urls)),
)
