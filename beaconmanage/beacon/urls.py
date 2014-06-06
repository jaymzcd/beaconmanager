from django.conf.urls import patterns, url
from .views import BeaconAddView


urlpatterns = patterns('',
    url(r'^add/', BeaconAddView.as_view(), name='add'),
)
