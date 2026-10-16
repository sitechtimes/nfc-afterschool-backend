from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    caass_id = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    activity = models.ForeignKey(
        'Activity', 
        on_delete=models.CASCADE, 
        related_name='participants'
    )

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    scanner_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    duration = models.DurationField(default=datetime.timedelta(minutes=60))

    def __str__(self):
        return self.name