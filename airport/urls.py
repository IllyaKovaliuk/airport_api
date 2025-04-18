from rest_framework import routers
from django.urls import path, include

from airport.views import AirportView

router = routers.DefaultRouter()
router.register('airports', AirportView)


urlpatterns = [
    path('', include(router.urls)),
]


app_name = 'airport'