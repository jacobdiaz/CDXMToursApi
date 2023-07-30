from django.db import models
DEFAULT_GOOGLE_MAPS_LINK = "https://goo.gl/maps/7r4jXBxTbU3V6RQS7"

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