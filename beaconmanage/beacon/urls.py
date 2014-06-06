from django.conf.urls import patterns, url
from .views import BeaconCreateView


urlpatterns = patterns('',
    url(r'^add/', BeaconCreateView.as_view(), name='add'),
)
