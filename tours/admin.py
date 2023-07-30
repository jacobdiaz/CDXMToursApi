from django.contrib import admin
from .models import TourLocation, Tour

class TourAdmin(admin.ModelAdmin):
    def duplicate_tour(modeladmin, request, queryset):
        for tour in queryset:  # Iterate through the selected tours
            tour.pk = None  # Set the primary key to None to create a new object
            # Swap the locales
            if tour.locales == 'en':
                tour.locales = 'es'
            else:
                tour.locales = 'en'
            tour.save()  # Save the new object to the database

    duplicate_tour.short_description = "Duplicate selected tours"

    list_display = ('id', 'tour_name', 'locales',
                    'availability_type', 'duration', 'price', 'order')
    ordering = ['order']  # Order the tours based on the 'order' field
    actions = [duplicate_tour]  # Add the custom action here

    # Customize the form layout using fieldsets
    fieldsets = [
        ('Tour Information', {
            'fields': [
                'tour_name',
                'locales',
                'availability_type',
                'availability',
                'price',
                'duration',
                'cap',
                'description',
                'included',
                'location',
            ],
        }),
        # ('Card Image', {
        #     'fields': ['card_image'],
        # }),
        # ('Tour Gallery Images', {
        #     'fields': [
        #         'gallery_image_1',
        #         'gallery_image_2',
        #         'gallery_image_3',
        #         'gallery_image_4',
        #         'gallery_image_5',
        #     ],
        # }),
        ('Order', {
            'fields': ['order'],
        }),
    ]



class TourLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'google_maps_link',
                    'lat', 'lon')


admin.site.register(Tour, TourAdmin)
admin.site.register(TourLocation, TourLocationAdmin,)
