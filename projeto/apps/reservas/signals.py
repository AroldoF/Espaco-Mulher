from django.db.models.signals import post_delete, pre_save
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
    # Apenas restaurar o estoque quando a reserva for deletada
    if instance.quantidade_comprada:
        instance.produto.estoque += instance.quantidade_comprada
        instance.produto.save()


@receiver(pre_save, sender=ReservaProduto)
def ajustar_estoque(sender, instance, **kwargs):
    """Ajusta o estoque quando a quantidade comprada muda"""
    if instance.pk:  # Verifica se é uma atualização de uma reserva existente
        reserva_antiga = ReservaProduto.objects.get(pk=instance.pk)
        if reserva_antiga.quantidade_comprada != instance.quantidade_comprada:
            # Ajustar o estoque
            instance.produto.estoque += reserva_antiga.quantidade_comprada  # Retorna o estoque antigo
            instance.produto.estoque -= instance.quantidade_comprada  # Subtrai a nova quantidade
            instance.produto.save()