from django.contrib import admin
from .models import TourLocation

class TourLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'google_maps_link',
                    'lat', 'lon')

admin.site.register(TourLocation, TourLocationAdmin,)
