from rest_framework import serializers

from airport.models import Airport, Route


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


class RouteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ("id", "source", "destination", "distance")


class RouteRetrieveSerializer(RoutesSerializer):
    class Meta:
        model = Route
        fields = ("source", "destination")