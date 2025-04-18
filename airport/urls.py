from rest_framework import routers
from django.urls import path, include

from airport.views import AirportViewSet, RouteViewSet, AirportViewSet

router = routers.DefaultRouter()
router.register('airport', AirportViewSet)
router.register('routes', RouteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


app_name = 'airport'