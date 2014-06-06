from django.contrib import admin
from .models import Beacon, Location


class BeaconAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'major', 'minor', 'last_checkin', 'created_at', 'has_metadata')

    def has_metadata(self, obj):
        return len(obj.metadata) > 0
    has_metadata.boolean = True


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Beacon, BeaconAdmin)
admin.site.register(Location, LocationAdmin)
