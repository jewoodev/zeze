from django.db import models


class Flight(models.Model):
    departure_time = models.TimeField()
    destination = models.CharField(max_length=30)
    airline = models.CharField(max_length=15)
    flight_number = models.CharField(max_length=15)
    terminal = models.CharField(max_length=5)
    gate = models.CharField(max_length=10)
    date = models.DateField()


