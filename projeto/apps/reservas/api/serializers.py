from rest_framework import serializers
from apps.reservas.models import ReservaProduto, ReservaServico
from apps.produtos.models import Produto
from apps.servicos.models import Servico
from django.contrib.auth.models import User

class UserResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class ProdutoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome']  # Exibir apenas ID e Nome

class ReservaProdutoSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), write_only=True
    )  # Aceita apenas ID na criação
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )
    class Meta:
        model = ReservaProduto
        fields = ['id','user', 'produto', 'quantidade_comprada', 'data_reservada', 'disponivel']

    def to_representation(self, instance):
        """Retorna os detalhes do produto na leitura"""
        data = super().to_representation(instance)
        data['user'] = UserResumoSerializer(instance.user).data
        data['produto'] = ProdutoResumoSerializer(instance.produto).data  # Substitui ID por detalhes
        return data
    
class ServicoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome','tempo_duracao']  # Exibir apenas ID e Nome

class ReservaServicoSerializer(serializers.ModelSerializer):
    servico = serializers.PrimaryKeyRelatedField(
        queryset=Servico.objects.all(), write_only=True
    )  # Aceita apenas ID na criação
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )
    class Meta:
        model = ReservaServico
        fields = ['id', 'user', 'servico', 'data_reservada','disponivel']

    def to_representation(self, instance):
        """Retorna os detalhes do produto na leitura"""
        data = super().to_representation(instance)
        data['user'] = UserResumoSerializer(instance.user).data
        data['servico'] = ServicoResumoSerializer(instance.servico).data  # Substitui ID por detalhes
        return data