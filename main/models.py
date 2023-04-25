from django.db import models


class Flight(models.Model):
    departure_time = models.TimeField()
    destination = models.CharField(max_length=30)
    airline = models.CharField(max_length=15)
    flight_number = models.CharField(max_length=15)
    terminal = models.CharField(max_length=5)
    gate = models.CharField(max_length=10)
    date = models.DateField()
    # def __str__(self):
    #     return str.name

# class Data(models.Model):
#     specific_id = models.CharField('specific_id', max_length=156)
#     horizon_width = models.CharField('horizon_width', max_length=100)
#     vertical_width = models.CharField('vertical_width', max_length=100)
#     x_location = models.CharField('x_location', max_length=100)
#     y_location = models.CharField('y_location', max_length=100)
#     def __str__(self):
#         return str(self.specific_id)


