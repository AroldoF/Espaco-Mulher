from django.db import models
from django.contrib.auth.models import User
from apps.produtos.models import Produto
from apps.servicos.models import Servico

class ReservaProduto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_comprada = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disponivel = models.BooleanField(default=False)
    data_reservada = models.DateTimeField()

    def calc_valor(self):
        # Calculando o valor total com base no preço do produto e quantidade comprada
        self.valor_total = self.produto.preco * self.quantidade_comprada

    def save(self, *args, **kwargs):
        self.calc_valor()  # Calcula o valor total antes de salvar
        super().save(*args, **kwargs)  # Salva o objeto

    def __str__(self):
        return f"Reserva de produto: {self.produto.nome} para {self.user.username}"

class ReservaServico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE) 
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disponivel = models.BooleanField(default=False)
    data_reservada = models.DateTimeField()

    def calc_valor(self):
        # Calculando o valor total com base no preço do serviço (produto) associado
        self.valor_total = self.servico.preco

    def save(self, *args, **kwargs):
        self.calc_valor()  # Calcula o valor total antes de salvar
        super().save(*args, **kwargs)  # Salva o objeto

    def __str__(self):
        return f"Reserva de serviço: {self.servico.nome} para {self.user.username}"
