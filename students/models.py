from django.db import models
from activities.models import Activity

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    caass_id = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE, 
        related_name='participants'
    )

    def __str__(self):
        return self.name