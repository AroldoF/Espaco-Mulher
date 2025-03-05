from django.urls import path
from apps.reservas.views import agenda,reservas,reservas_produto,reservas_servico,editar_reserva_produto,\
    editar_reserva_servico,deletar_reserva_produto,deletar_reserva_servico

urlpatterns = [
    path('agenda/', agenda, name='agenda'),
    path('reservas/', reservas, name='reservas'),
    path('reservas-produto/<int:id>', reservas_produto, name='reservas-produto'),
    path('reservas-servico/<int:id>', reservas_servico, name='reservas-servico'),
    path('editar-reservas-produto/<int:id>', editar_reserva_produto, name='editar-reservas-produto'),
    path('editar-reservas-servico/<int:id>', editar_reserva_servico, name='editar-reservas-servico'),
    path('deletar-reserva-produto/<int:id>', deletar_reserva_produto, name='deletar-reserva-produto'),
    path('deletar-reserva-servico/<int:id>', deletar_reserva_servico, name='deletar-reserva-servico'),
]
