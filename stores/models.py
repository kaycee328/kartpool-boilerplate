from django.db import models
from django.contrib.gis.db import models

from django.contrib.gis.geos import Point
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    rating = models.FloatField(
        null=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    store_type = models.CharField(null=True, max_length=50)
    opening_hour = models.TimeField(null=True)
    closing_hour = models.TimeField(null=True)
    city = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location = models.PointField(null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(null=True, max_length=100)

    # def save(self, *args, **kwargs):
    #     if self.latitude is not None and self.longitude is not None:
    #         self.location = Point(self.longitude, self.latitude)
    #     elif self.location is not None:
    #         self.latitude = self.location.y
    #         self.longitude = self.location.x
    #     super(Store, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


# from django.db import models
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
# from django.core.validators import MaxValueValidator, MinValueValidator
