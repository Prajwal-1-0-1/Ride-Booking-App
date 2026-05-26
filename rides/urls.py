from django.urls import path
from .views import *

urlpatterns = [
    
    path('create-ride/<int:rider_id>/', create_ride),
    path('start-ride/<int:ride_id>/', start_ride),
    path('complete-ride/<int:ride_id>/', complete_ride),
    path('cancel-ride/<int:ride_id>/', cancel_ride),
]