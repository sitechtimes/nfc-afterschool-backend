from django.shortcuts import render
from .models import Activity
from rest_framework import viewsets
from .serialilzers import ActivitySerializer

# Create your views here.
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer