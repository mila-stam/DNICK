from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pilot(models.Model):
    RANK_CHOICES = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior")
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    yearBirth = models.IntegerField()
    totalFlightHours = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.CharField(max_length=1, choices=RANK_CHOICES)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Baloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small Baloon"),
        ("M", "Medium Baloon"),
        ("L", "Large Baloon")
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=100)
    maxPassengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.manufacturer}"
    
class Airline(models.Model):
    name = models.CharField(max_length=100)
    yearFounded = models.IntegerField()
    outsideEurope = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.yearFounded}"
    
class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} {self.pilot}"

class Flight(models.Model):
    code = models.CharField(max_length=100, unique=True)
    takeOffAirport = models.CharField(max_length=100)
    landAirport = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="flight_photos/", null=True, blank=True)
    baloon = models.ForeignKey(Baloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.takeOffAirport} {self.landAirport}"