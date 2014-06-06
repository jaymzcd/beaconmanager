from django.db import models
from django.core.urlresolvers import reverse


class Location(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __unicode__(self):
        return '{}'.format(self.name)

class Beacon(models.Model):
    uuid = models.CharField(max_length=128, unique=True)
    major = models.CharField(max_length=10, blank=True, null=True)
    minor = models.CharField(max_length=10, blank=True, null=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    last_checkin = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{}'.format(self.uuid)

    def get_absolute_url(self):
        # http://stackoverflow.com/a/1720961
        return reverse('admin:%s_%s_change' % (self._meta.app_label,   self._meta.module_name),  args= [self.id])
