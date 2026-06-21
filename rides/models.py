from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Rider(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Ride(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    pickup_lat = models.FloatField()
    pickup_lon = models.FloatField()
    drop_lat = models.FloatField()
    drop_lon = models.FloatField()
    status = models.CharField(max_length=20, choices=[
                                ("REQUESTED", "REQUESTED"),
                                ("ASSIGNED", "ASSIGNED"),
                                ("ONGOING", "ONGOING"),
                                ("COMPLETED", "COMPLETED"),
                                ("CANCELLED", "CANCELLED"),
                             ], default="REQUESTED")
    ride_type = models.CharField(max_length=20,default="normal",choices=[("NORMAL","NORMAL") , ("LUXURY","LUXURY")])  #luxury or normal
    fare = models.FloatField()
    def __str__(self):
        return f"Ride {self.id}"
    

    class User(models.Model):

        ROLE_CHOICES = [
            ("RIDER", "Rider"),
            ("DRIVER", "Driver")
        ]

        username = models.CharField(max_length=100, unique=True)

        password = models.CharField(max_length=255)

        role = models.CharField(
            max_length=20,
            choices=ROLE_CHOICES
    )