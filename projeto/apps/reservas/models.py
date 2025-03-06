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
        """Calcula o valor total baseado no preço do produto e quantidade comprada"""
        self.valor_total = self.produto.preco * self.quantidade_comprada

    def save(self, *args, **kwargs):
        """Garante a atualização do estoque ao criar ou editar uma reserva"""
        if self.pk:  # Se a reserva já existe (edição)
            reserva_antiga = ReservaProduto.objects.get(pk=self.pk)
            diferenca = self.quantidade_comprada - reserva_antiga.quantidade_comprada

            if diferenca > 0:  # Se a quantidade aumentou
                if self.produto.estoque >= diferenca:
                    self.produto.estoque -= diferenca
                else:
                    raise ValueError("Estoque insuficiente para a alteração.")  # Caso o estoque não seja suficiente
            elif diferenca < 0:  # Se a quantidade diminuiu
                self.produto.estoque += abs(diferenca)  # Retorna o estoque para o produto
            # Caso a quantidade não tenha mudado, não alteramos o estoque.

        else:  # Nova reserva
            if self.produto.estoque >= self.quantidade_comprada:
                self.produto.estoque -= self.quantidade_comprada
            else:
                raise ValueError("Estoque insuficiente para a reserva.")  # Caso o estoque não seja suficiente

        self.produto.save()
        self.calc_valor()  # Calcular valor total da reserva
        super().save(*args, **kwargs)  # Salvar normalmente


    def __str__(self):
        return f"Reserva de produto: {self.produto.nome} para {self.user.username}"


class ReservaServico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE) 
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disponivel = models.BooleanField(default=False)
    data_reservada = models.DateTimeField()

    def calc_valor(self):
        """Calcula o valor total com base no preço do serviço"""
        self.valor_total = self.servico.preco

    def save(self, *args, **kwargs):
        self.calc_valor()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva de serviço: {self.servico.nome} para {self.user.username}"
