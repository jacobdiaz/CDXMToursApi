# Generated by Django 4.2.3 on 2023-07-30 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tour_name', models.CharField(max_length=255)),
                ('locales', models.CharField(choices=[('en', 'English'), ('es', 'Spanish')], default='en', help_text='Select the language of this tour', max_length=2)),
                ('availability_type', models.CharField(choices=[('Weekday', 'Weekday'), ('Weekend', 'Weekend'), ('Reservation', 'Reservation')], default='Weekday', help_text='When will this tour be available?', max_length=255)),
                ('availability', models.CharField(default='Mon - Fri (10:00am)', help_text='What days and times will this tour be available?', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=950.0, help_text='Price in MXN', max_digits=8)),
                ('duration', models.CharField(default='2 hours', max_length=255)),
                ('cap', models.PositiveIntegerField(default=10, verbose_name='Tour Persons Capacity')),
                ('description', models.TextField(default='This is a tour description')),
                ('included', models.TextField(default='Included: Bikes, Helmets, Tacos, Hydration')),
                ('order', models.PositiveIntegerField(default=0, help_text='This is the order in which the tour shows up on the page. Leave order as 0 to place this tour in the end of the list.')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tours.tourlocation', verbose_name='Tour Location')),
            ],
        ),
    ]
