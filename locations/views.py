from django.shortcuts import render
from .models import Location
from .serializer import LocationSerializer
from rest_framework import viewsets

# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer