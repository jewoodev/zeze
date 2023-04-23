from django.db import models


class Flight(models.Model):
    date = models.DateField()
    time = models.TimeField()
    destination = models.CharField(max_length=15)
    airline = models.CharField(max_length=15)
    flight_number = models.CharField(max_length=15)


