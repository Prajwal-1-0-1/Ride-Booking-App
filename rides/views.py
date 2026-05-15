from django.http import JsonResponse
from django.db import transaction
from .models import Rider, Ride, Driver
from django.views.decorators.csrf import csrf_exempt
from .utils import *
import json

@csrf_exempt
@transaction.atomic
def create_ride(request,rider_id):
        
        if request.method != "POST":
            return JsonResponse({"error": "Only POST allowed"})

        rider = Rider.objects.select_for_update().get(id=rider_id)
        if not rider:
            return JsonResponse({"error" : "rider not found"})
        
        data = json.loads(request.body)

        

        ride = Ride.objects.create(
            rider=rider,
            driver=None,
            pickup_lat=data["pickup_lat"],
            pickup_lon=data["pickup_lon"],
            drop_lat=data["drop_lat"],
            drop_lon=data["drop_lon"],
            status="REQUESTED",
            ride_type = data["ride_type"],
            fare= 0
        )

        driver = get_nearest_driver(ride.pickup_lat,ride.pickup_lon)
        driver.save()

        if not driver:
            return JsonResponse({"error": "No drivers available"})
        
        driver.is_available = False
        driver.save()

        ride.status = "ASSIGNED"
        ride.driver = driver
        if ride.ride_type == "LUXURY":
            ride.fare= 30 + (dist(ride.pickup_lat,ride.drop_lat,ride.pickup_lon,ride.drop_lon))*10
        elif ride.ride_type == "NORMAL":
            ride.fare= 30 + (dist(ride.pickup_lat,ride.drop_lat,ride.pickup_lon,ride.drop_lon))*15
        ride.save()

        return JsonResponse({
        "message": "Ride created",
        "ride_id": ride.id
        })


@csrf_exempt
@transaction.atomic
def start_ride(request, ride_id):

    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"})
        
    try:
        ride = Ride.objects.select_for_update().get(id=ride_id)


        if ride.status != "ASSIGNED":
            return JsonResponse({"error": "Ride cannot be started"})

        ride.status = "ONGOING"
        ride.save()  

        return JsonResponse({"message": "Ride started"})

    except Ride.DoesNotExist:
        return JsonResponse({"error": "Ride not found"})
    

@csrf_exempt
@transaction.atomic
def complete_ride(request,ride_id):

    if request.method != "POST":
         return JsonResponse({"error": "Only POST allowed"})
    try:
        ride = Ride.objects.select_for_update().get(id=ride_id)
        driver = ride.driver

        ride.status = "COMPLETED"
        ride.save()

        driver.is_available = True
        driver.latitude = ride.drop_lat
        driver.longitude = ride.drop_lon
        driver.save()

        return JsonResponse({"message": "Ride completed"})

    except Ride.DoesNotExist:
         return JsonResponse({"error": "Ride not found"})
    

@csrf_exempt
@transaction.atomic 
def cancel_ride(request,ride_id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"})
    try:
         ride = Ride.objects.select_for_update().get(id = ride_id)
         driver = ride.driver

         ride.status = "CANCELLED"
         ride.save()

         driver.is_available = True
         driver.save()

         return JsonResponse({"message" : "Ride Cancelled"})
    
    except Ride.DoesNotExist:
         return JsonResponse({"error": "Ride not found"})
    

