from django.shortcuts import render
from rest_framework import viewsets

from airport.models import Airport, Route, Airplane, AirplaneType, Flight, Ticket, Order
from airport.serializers import AirportSerializer, AirportRetrieveSerializer, AirportListSerializer, \
    RouteListSerializer, RouteRetrieveSerializer, RoutesSerializer, AirplaneListSerializer, AirplaneRetrieveSerializer, \
    AirplaneSerializer, AirplaneTypeSerializer, AirplaneTypeListSerializer, AirplaneTypeRetrieveSerializer, \
    FlightListSerializer, FlightRetrieveSerializer, FlightSerializer, TicketSerializer, OrderSerializer


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AirportListSerializer
        elif self.action == 'retrieve':
            return AirportRetrieveSerializer
        return AirportSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RouteListSerializer
        elif self.action == 'retrieve':
            return RouteRetrieveSerializer
        return RoutesSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AirplaneListSerializer
        elif self.action == 'retrieve':
            return AirplaneRetrieveSerializer
        return AirplaneSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneTypeListSerializer
        elif self.action == "retrieve":
            return AirplaneTypeRetrieveSerializer
        return AirplaneTypeSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer
        elif self.action == "retrieve":
            return FlightRetrieveSerializer
        return FlightSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer