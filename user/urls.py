from django.urls import path

from user.views import CreateUserView, LoginUserView, UpdateUserView
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='create'),
    path('login/', LoginUserView.as_view(), name='get_token'),
    path('me/', UpdateUserView.as_view(), name='manage_user'),
]

app_name = 'user'