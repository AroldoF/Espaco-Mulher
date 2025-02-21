from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Produto(models.Model):
    # OPCOES_CATEGORIA = [
    #     ("ELETRÔNICOS","Eletrônicos"),
    #     ("ROUPAS", "Roupas"),
    #     ("ACESSÓRIOS", "Acessórios"),
    #     ("DECORAÇÃO", "Decoração"),
    # ]
    nome = models.CharField(max_length=200,blank=False,null=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    #categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='ELETRÔNICOS')
    foto = models.ImageField(null=False)

    def __str__(self):
        return self.nome

class ReservaProdutos():
    user = models.ForeignKey(User)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    # data_reservada = models.ForeignKey(Produto, on_delete=models.CASCADE)