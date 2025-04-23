from rest_framework import routers
from django.urls import path, include

from airport.views import AirportViewSet, RouteViewSet, AirportViewSet, AirplaneViewSet, AirplaneTypeViewSet, \
    FlightViewSet, TicketViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('airport', AirportViewSet)
router.register('routes', RouteViewSet)
router.register('planes', AirplaneViewSet)
router.register('airplanetype', AirplaneTypeViewSet)
router.register("flights", FlightViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
]


app_name = 'airport'