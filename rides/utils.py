from .models import Rider, Ride, Driver
from django.db import connection
import math
from math import radians, sin, cos, sqrt, atan2

def dist(lat1,lat2,lon1,lon2):
    d = (lat1-lat2)**2 + (lon1-lon2)**2
    return math.sqrt(d)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def get_nearest_driver(pickup_lat,pickup_lon):

        drivers = Driver.objects.filter(
            is_available=True,
            latitude__gte=pickup_lat - 0.05,
            latitude__lte=pickup_lat + 0.05,
            longitude__gte=pickup_lon - 0.05,
            longitude__lte=pickup_lon + 0.05,
        )
        nearest = None
        mini = 1e9

        for driver in drivers:
              dist = haversine(pickup_lat,pickup_lon,driver.latitude,driver.longitude)
              if dist < mini :
                    mini = dist
                    nearest = driver
              
        return nearest
