# Generated by Django 4.2.3 on 2023-07-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('google_maps_link', models.CharField(default='https://goo.gl/maps/7r4jXBxTbU3V6RQS7', max_length=255)),
                ('lat', models.DecimalField(decimal_places=6, default='19.42755', help_text='Find Latitude and Longitude at https://www.latlong.net/', max_digits=9, verbose_name='Latitude')),
                ('lon', models.DecimalField(decimal_places=6, default='-99.15569', help_text='Find Latitude and Longitude at https://www.latlong.net/', max_digits=9, verbose_name='Longitude')),
            ],
        ),
    ]
