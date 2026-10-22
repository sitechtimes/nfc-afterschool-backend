from django.db import models
from locations.models import Location
import datetime

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    duration = models.DurationField(default=datetime.timedelta(minutes=60))

    def __str__(self):
        return self.name