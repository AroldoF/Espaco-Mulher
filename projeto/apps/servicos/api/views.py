from rest_framework import viewsets, generics, filters
from apps.servicos.models import Servico
from apps.servicos.api.serializers import ServicoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all().order_by('id')
    serializer_class = ServicoSerializer
    ordering_fields = ['id','nome','preco']
    search_fields = ['nome',]