from django.db import models
from .modelchoices import *
DEFAULT_GOOGLE_MAPS_LINK = "https://goo.gl/maps/7r4jXBxTbU3V6RQS7"

class Tour(models.Model):
    #! Columns
    id = models.AutoField(primary_key=True, unique=True)
    tour_name = models.CharField(max_length=255)
    locales = models.CharField(
        max_length=2,
        choices=LOCALES_CHOICES,
        default="en",
        help_text="Select the language of this tour",
    )
    availability_type = models.CharField(
        max_length=255,
        choices=AVAILABLE_TYPE_CHOICES,
        default="Weekday",
        help_text="When will this tour be available?",
    )
    availability = models.CharField(
        max_length=255,
        default="Mon - Fri (10:00am)",
        help_text="What days and times will this tour be available?",
    )
    price = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="Price in MXN", default=950.00
    )
    duration = models.CharField(max_length=255, default="2 hours")
    cap = models.PositiveIntegerField(
        verbose_name="Tour Persons Capacity",
        default=10)
    description = models.TextField(default="This is a tour description")
    included = models.TextField(
        default="Included: Bikes, Helmets, Tacos, Hydration")

    # Add the TourLocation OneToOneField
    location = models.ForeignKey(
        'TourLocation',  # Use quotes to reference the model string
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Tour Location'
    )

    order = models.PositiveIntegerField(
        default=0, help_text="This is the order in which the tour shows up on the page. Leave order as 0 to place this tour in the end of the list.",
    )

class TourLocation(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    address = models.CharField(max_length=255)
    google_maps_link = models.CharField(
        max_length=255, default=DEFAULT_GOOGLE_MAPS_LINK)
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name="Latitude",
        default="19.42755",
        help_text="Find Latitude and Longitude at https://www.latlong.net/")
    lon = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name="Longitude",
        default="-99.15569",
        help_text="Find Latitude and Longitude at https://www.latlong.net/")

    def __str__(self):
        return self.address 