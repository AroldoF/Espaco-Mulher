from rest_framework import viewsets, generics, filters
from apps.reservas.models import ReservaProduto,ReservaServico
from apps.reservas.api.serializers import ReservaProdutoSerializer,ReservaServicoSerializer

class ReservaProdutoViewSet(viewsets.ModelViewSet):
    queryset = ReservaProduto.objects.all().order_by('id')
    serializer_class = ReservaProdutoSerializer
    ordering_fields = ['id','produto','user']
    search_fields = ['data_reservada',]

class ReservaServicoViewSet(viewsets.ModelViewSet):
    queryset = ReservaServico.objects.all().order_by('id')
    serializer_class = ReservaServicoSerializer
    ordering_fields = ['id','produto','user']
    search_fields = ['data_reservada',]