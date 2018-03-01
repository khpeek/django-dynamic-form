from django.db import models
from django.urls import reverse
from django.utils import timezone


class CheckInType(models.Model):
    title = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
    	return self.title


class CheckIn(models.Model):
    checkin_type = models.ForeignKey(CheckInType, null=True, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)

    notes = models.TextField(blank=True)

    # Scheduling
    requested_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
    	return reverse('checkin-detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
    	if not self.id:
    		self.requested_date = timezone.now()
    	super().save(*args, **kwargs)