from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry

from .models import Store


def get_nearby_stores_within(
    latitude: float, longitude: float, km: int = 10, limit: int = None, srid: int = 4326
):
    coordinates = Point(longitude, latitude, srid=srid)
    point = GEOSGeometry(coordinates, srid=4326)
    return (
        Store.objects.annotate(distance=Distance("location", coordinates))
        .filter(location__distance_lte=(point, D(km=km)))
        .order_by("distance")[0:limit]
    )


def get_nearby_stores_within(
    latitude: float, longitude: float, km: int = 10, limit: int = None, srid: int = 4326
):
    # Create a Point object from the provided longitude and latitude
    coordinates = Point(longitude, latitude, srid=srid)
    # Convert to GEOSGeometry with the specified SRID
    point = GEOSGeometry(coordinates, srid=4326)
    # Query the Store model to find nearby stores
    queryset = Store.objects.annotate(distance=Distance("location", point))
    nearby_stores = queryset.filter(location__distance_lte=(point, D(km=km)))
    # Order by distance and apply limit if provided
    nearby_stores = nearby_stores.order_by("distance")
    if limit:
        nearby_stores = nearby_stores[:limit]
    return nearby_stores
