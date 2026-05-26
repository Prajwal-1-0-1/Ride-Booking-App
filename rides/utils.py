from .models import Rider, Ride, Driver
from django.db import connection
import math

def dist(lat1,lat2,lon1,lon2):
    d = (lat1-lat2)**2 + (lon1-lon2)**2
    return math.sqrt(d)


def get_nearest_driver(pickup_lat,pickup_lon):
     
        drivers = Driver.objects.filter(is_available = True)
        nearest = None
        mini = 1e9

        for driver in drivers:
              dist = math.sqrt((driver.latitude-pickup_lat)**2 + (driver.longitude-pickup_lon)**2)

              if dist < mini :
                    mini = dist
                    nearest = driver
              
        return nearest
