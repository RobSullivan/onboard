from django.db import models

# Create your models here.
class Passenger(models.Model):
	bus_route = models.CharField(max_length=7)
	bus_stop = models.CharField(max_length=5)
	is_waiting = models.BooleanField