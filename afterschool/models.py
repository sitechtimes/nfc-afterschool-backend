from django.db import models
import datetime

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    scanner_device_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    duration = models.DurationField(default=datetime.timedelta(minutes=60))

    def __str__(self):
        return self.name