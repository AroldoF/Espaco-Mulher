from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
from .models import ReservaProduto

@receiver(pre_save, sender=ReservaProduto)
def atualizar_valor_reserva_produto(sender, instance, **kwargs):
    """Atualiza o valor total sempre que a reserva for salva"""
    instance.calc_valor()  # Apenas calcular o valor sem chamar save()
    # Não é necessário salvar aqui porque o valor será salvo no método save() do modelo


@receiver(post_delete, sender=ReservaProduto)
def restaurar_estoque(sender, instance, **kwargs):
    """Devolve o estoque ao excluir uma reserva"""
    instance.produto.estoque += instance.quantidade_comprada
    instance.produto.save()
