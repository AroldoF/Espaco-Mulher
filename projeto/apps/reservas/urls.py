from django.urls import path
from apps.reservas.views import calendario

urlpatterns = [
    path('calendario/', calendario, name='calendario'),
]
