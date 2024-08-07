# Generated by Django 5.0.7 on 2024-08-07 17:08

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('store_type', models.CharField(max_length=50, null=True)),
                ('opening_hour', models.TimeField(null=True)),
                ('closing_hour', models.TimeField(null=True)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
