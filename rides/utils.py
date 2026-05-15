from .models import Rider, Ride, Driver
from django.db import connection
import math

def dist(lat1,lat2,lon1,lon2):
    d = (lat1-lat2)**2 + (lon1-lon2)**2
    return math.sqrt(d)


def get_nearest_driver(pickup_lat,pickup_lon):
     
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id
                FROM rides_driver
                WHERE is_available = TRUE
                ORDER BY
                ST_SetSRID(
                    ST_MakePoint(longitude, latitude),
                    4326
                ) <-> 
                ST_SetSRID(
                    ST_MakePoint(%s, %s),
                    4326
                )
                LIMIT 1;
            """, [pickup_lon, pickup_lat])

            row = cursor.fetchone()

            row_id = row[0]

            if not row:
                return none

        return Driver.objects.get(id = row_id)