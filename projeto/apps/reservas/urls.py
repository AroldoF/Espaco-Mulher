from django.urls import path
from apps.reservas.views import calendario,reservas,reservas_produto,reservas_servico

urlpatterns = [
    path('calendario/', calendario, name='calendario'),
    path('reservas/', reservas, name='reservas'),
    path('reservas-produto/<int:id>', reservas_produto, name='reservas-produto'),
    path('reservas-servico/<int:id>', reservas_servico, name='reservas-servico'),
]
