from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from airport.models import (
    Airport,
    Route,
    Airplane,
    AirplaneType,
    Flight,
    Ticket,
    Order
)
from user.models import User


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class AirportListSerializer(AirportSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class AirportRetrieveSerializer(AirportSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class RoutesSerializer(serializers.ModelSerializer):
    source_id = serializers.PrimaryKeyRelatedField(
        queryset=Airport.objects.all(), write_only=True, source="source"
    )
    destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Airport.objects.all(), write_only=True, source="destination"
    )
    source = serializers.CharField(source='source.name', read_only=True)
    destination = serializers.CharField(source='destination.name', read_only=True)
    class Meta:
        model = Route
        fields = ("id", "source_id", "destination_id", "source", "destination", "distance")


class RouteListSerializer(RoutesSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class RouteRetrieveSerializer(RoutesSerializer):
    class Meta:
        model = Route
        fields = ("source", "destination")


class AirplaneTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type = serializers.SlugRelatedField(
        queryset=AirplaneType.objects.all(),
        slug_field="name",
    )

    class Meta:
        model = Airplane
        fields = ("id","name", "seats_in_row", "rows", "airplane_type")


class AirplaneListSerializer(AirplaneSerializer):
    class Meta:
        model = Airplane
        fields = ("name", "seats_in_row", "rows", "airplane_type")


class AirplaneRetrieveSerializer(AirplaneSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"


class AirplaneTypeRetrieveSerializer(AirplaneTypeSerializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirplaneTypeListSerializer(AirplaneTypeSerializer):
    class Meta:
        model = AirplaneType
        fields = ("name",)


class FlightSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    class Meta:
        model = Flight
        fields = "__all__"


class FlightRetrieveSerializer(FlightSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class FlightListSerializer(FlightSerializer):
    route_source = serializers.CharField(source="route.source")
    route_destination = serializers.CharField(source="route.destination")
    plane = serializers.CharField(source="airplane.name")
    status = serializers.ReadOnlyField()

    class Meta:
        model = Flight
        fields = ("id", "departure_time", "arrival_time", "route_source", "route_destination", "plane", "status")


class TicketSerializer(serializers.ModelSerializer):
    airplane = serializers.CharField(source="flight.airplane.name", read_only=True)
    flight = serializers.PrimaryKeyRelatedField(
        queryset=Flight.objects.all()
    )
    # order = OrderSerializer(read_only=True)
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        source="order.user"
    )
    user_order_token = serializers.SlugRelatedField(
        slug_field="token",
        read_only=True,
        source="order"
    )
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "airplane", "flight", "order", "user", "user_order_token")

        validators = [
            UniqueTogetherValidator(
                queryset=Ticket.objects.all(),
                fields=("seat", "flight"),
            )
        ]

    def validate(self, attrs):
        flight = attrs.get("flight")

        if not flight:
            raise serializers.ValidationError({"flight": "Flight is required."})

        if flight.status in ['finished', 'active']:
            raise serializers.ValidationError({
                "flight": f"Cannot book ticket for a flight that is {flight.status}."
            })

        airplane = flight.airplane  # доступ до літака через рейс

        Ticket.validate_seats(
            row=attrs["row"],
            rows=airplane.rows,
            seat=attrs["seat"],
            seats_in_row=airplane.seats_in_row,
            error_to_raise=serializers.ValidationError
        )
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    token = serializers.ReadOnlyField()
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )
    class Meta:
        model = Order
        fields = ("id", "token", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['user'].queryset = User.objects.filter(id=request.user.id)
