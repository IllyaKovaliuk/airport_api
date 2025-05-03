from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from airport.models import Airport, Route, Airplane, AirplaneType, Flight, Ticket, Order
from airport.permissions import IsAdminOrIsAuthenticatedReadOnly, IsAdminOrReadOnly
from airport.serializers import (
    AirportSerializer,
    AirportRetrieveSerializer,
    AirportListSerializer,
    RouteListSerializer,
    RouteRetrieveSerializer,
    RoutesSerializer,
    AirplaneListSerializer,
    AirplaneRetrieveSerializer,
    AirplaneSerializer,
    AirplaneTypeSerializer,
    AirplaneTypeListSerializer,
    AirplaneTypeRetrieveSerializer,
    FlightListSerializer,
    FlightRetrieveSerializer,
    FlightSerializer,
    TicketSerializer,
    OrderSerializer
)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return AirportListSerializer
        elif self.action == 'retrieve':
            return AirportRetrieveSerializer
        return AirportSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return RouteListSerializer
        elif self.action == 'retrieve':
            return RouteRetrieveSerializer
        return RoutesSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return AirplaneListSerializer
        elif self.action == 'retrieve':
            return AirplaneRetrieveSerializer
        return AirplaneSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminOrReadOnly]


    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneTypeListSerializer
        elif self.action == "retrieve":
            return AirplaneTypeRetrieveSerializer
        return AirplaneTypeSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer
        elif self.action == "retrieve":
            return FlightRetrieveSerializer
        return FlightSerializer


class TicketViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        return self.queryset.filter(order__user=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)