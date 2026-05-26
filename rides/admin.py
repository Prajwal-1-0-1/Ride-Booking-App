from django.contrib import admin
from .models import Ride, Driver, Rider

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pickup_lat',
        'pickup_lon',
        'drop_lat',
        'drop_lon',
        'status',
        'fare',
        'driver',
        'rider',
        'ride_type',
    )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'latitude',
        'longitude',
        'is_available',
    )


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
