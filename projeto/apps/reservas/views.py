from django.shortcuts import render,get_object_or_404
from apps.reservas.models import ReservaProduto, ReservaServico
from apps.servicos.models import Servico
from apps.produtos.models import Produto

def calendario(request):
    #reserva = Reserva.objects.order_by("id")
    return render(request, 'reservas/calendario.html')#, {"cards": reserva})

def reservas(request):
    reservaprodutos = ReservaProduto.objects.order_by("id")
    reservaservicos = ReservaServico.objects.order_by('id')
    return render(request, 'reservas/reservas.html', {'produtos': reservaprodutos, 'servicos': reservaservicos})

def reservas_produto(request,id):
    reservas = get_object_or_404(ReservaProduto, pk=id)
    produtos = get_object_or_404(Produto, pk=reservas.produto.id)
    return render(request, 'reservas/_reservas_id.html', {"reservas_produto": reservas,"produtos": produtos})

def reservas_servico(request,id):
    reservas = get_object_or_404(ReservaServico, pk=id)
    servicos = get_object_or_404(Servico, pk=reservas.servico.id)
    return render(request, 'reservas/_reservas_id.html', {"reservas_servico": reservas,"servicos": servicos})