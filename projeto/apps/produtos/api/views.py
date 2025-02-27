from apps.produtos.models import Produto
from apps.produtos.api.serializers import ProdutoSerializer
from rest_framework import viewsets, generics, filters

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    ordering_fields = ['id','nome','preco']
    search_fields = ['nome',]