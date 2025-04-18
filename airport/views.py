from django.shortcuts import render
from rest_framework import viewsets

from airport.models import Airport, Route
from airport.serializers import AirportSerializer, AirportRetrieveSerializer, AirportListSerializer, \
    RouteListSerializer, RouteRetrieveSerializer, RoutesSerializer


# Create your views here.
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AirportListSerializer
        elif self.action == 'retrieve':
            return AirportRetrieveSerializer
        return AirportSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return RouteListSerializer
        elif self.action == 'retrieve':
            return RouteRetrieveSerializer
        return RoutesSerializer