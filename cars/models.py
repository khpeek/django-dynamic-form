from django.db import models


class Manufacturer(models.Model):
	country = models.CharField(max_length=50)


class Car(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	country = models.CharField(max_length=50, blank=True)


