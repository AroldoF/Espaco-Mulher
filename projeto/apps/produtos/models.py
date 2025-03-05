from django.db import models

class Produto(models.Model):
    # OPCOES_CATEGORIA = [
    #     ("ELETRÔNICOS","Eletrônicos"),
    #     ("ROUPAS", "Roupas"),
    #     ("ACESSÓRIOS", "Acessórios"),
    #     ("DECORAÇÃO", "Decoração"),
    # ]
    nome = models.CharField(max_length=200,blank=False,null=False)
    descricao = models.TextField(null=True,blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    #categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='ELETRÔNICOS')
    foto = models.ImageField(upload_to='produtos/',null=True, blank=True)

    def __str__(self):
        return self.nome
