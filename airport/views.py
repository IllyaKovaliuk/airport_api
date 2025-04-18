from django.shortcuts import render
from rest_framework import viewsets

from airport.models import Airport
from airport.serializers import AirportSerializer


# Create your views here.
class AirportView(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer