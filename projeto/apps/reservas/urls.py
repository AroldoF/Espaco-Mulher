from django.urls import path
from apps.reservas.views import index

urlpatterns = [
    path('', index, name='index'),
]
