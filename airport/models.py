import hashlib

from django.db import models
from django.db.models import UniqueConstraint
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

from airport_project import settings
from user.models import User



class Airport(models.Model):
    name = models.CharField(max_length=255)
    closest_big_city = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination')
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.source.name} - {self.destination.name}"


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class AirplaneType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    @property
    def status(self) -> None:
        current_time = now()
        if self.arrival_time < current_time:
            return 'finished'
        elif self.departure_time > current_time:
            return 'not started'
        else:
            return 'active'



    def __str__(self):
        return f"Flight from {self.route.source} to {self.route.destination} with id: {self.route.id} "


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='tickets')

    constraints = [
        UniqueConstraint(fields=['seat', 'flight'], name='unique_ticket_seat_flight')
    ]

    @staticmethod
    def validate_seats(seat: int, seats_in_row: int, row: int, rows: int, error_to_raise):
        if not(1 <= seat <= seats_in_row):
            raise error_to_raise(
                {
                    'seat': f"seat must be in range [1, {seats_in_row}], not {seat}"
                }
            )
        elif not(1 <= row <= rows):
            raise error_to_raise(
                {
                    'row': f"row must be in range [1, {rows}], not {row}"
                }
            )

    def validate_flight(self):
        if not Flight.objects.filter(id=self.flight_id).exists():
            raise ValidationError(
                {
                    'flight': f"Flight {self.flight_id} does not exist"
                }
            )
        elif Flight.status in ['finished', 'active']:
            raise ValidationError(
                {
                    'flight': f"Flight finished or active now"
                }
            )

    def clean(self):
        Ticket.validate_seats(
            seat=self.seat,
            seats_in_row=self.flight.airplane.seats_in_row,
            row=self.row,
            rows=self.flight.airplane.rows,
            error_to_raise=ValidationError
        )
        self.validate_flight()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        return super(Ticket, self).save(force_insert, force_update, using, update_fields)


    def __str__(self):
        return f"Ticket - {self.flight.flight_id}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    @property
    def token(self):
        raw = f"{self.id}-{self.created_at}".encode()
        return hashlib.sha256(raw).hexdigest()[:10].upper()

    def __str__(self):
        return f"{self.user.username} - {self.token}"
