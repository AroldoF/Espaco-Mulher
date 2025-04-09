from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from apps.reservas.models import ReservaProduto, ReservaServico
from apps.reservas.forms import ReservaProdutoForms,ReservaServicoForms
from apps.servicos.models import Servico
from apps.produtos.models import Produto

from apps.servicos.forms import ServicoForm

def agenda(request):
    #reserva = Reserva.objects.order_by("id")
    return render(request, 'reservas/_agenda.html')#, {"cards": reserva})

def reservas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    # Filtrar apenas as reservas do usuário logado
    reservaprodutos = ReservaProduto.objects.filter(user=request.user).order_by("id")
    reservaservicos = ReservaServico.objects.filter(user=request.user).order_by("id")

    return render(request, 'reservas/reservas.html', {'produtos': reservaprodutos, 'servicos': reservaservicos})


def reservas_produto(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    # Busca a reserva, mas só se o usuário for o dono
    reservas = get_object_or_404(ReservaProduto, pk=id, user=request.user)

    # Busca o produto relacionado
    produtos = get_object_or_404(Produto, pk=reservas.produto.id)

    return render(request, 'reservas/_reservas_id.html', {"reservas_produto": reservas, "produtos": produtos})

def reservas_servico(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    # Busca a reserva, mas só se o usuário for o dono
    reservas = get_object_or_404(ReservaServico, pk=id, user=request.user)

    # Busca o serviço relacionado
    servicos = get_object_or_404(Servico, pk=reservas.servico.id)

    return render(request, 'reservas/_reservas_id.html', {"reservas_servico": reservas, "servicos": servicos})

def nova_reserva_produto(request, id):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    
    # produto = get_object_or_404(Produto, id=id)
    produto = Produto.objects.get(id=id)
    
    if request.method == 'POST':
        form = ReservaProdutoForms(request.POST, produto)  # Passa o produto para o formulário
        if form.is_valid():
            venda = form.save(commit=False)  
            venda.produto = produto  # Garante que o produto será salvo com a venda
            venda.user = request.user  # Atribui o usuário logado à reserva
            venda.save()  
            messages.success(request, 'Nova Reserva cadastrada!')
            return redirect('index')


    form = ReservaProdutoForms
    return render(request, 'reservas/_criar_reserva.html', {'form': form, 'produto':produto})

def editar_reserva_produto(request,id):
    produto = ReservaProduto.objects.get(pk=id)
    form = ReservaProdutoForms(instance=produto)

    if request.method == 'POST':
        form = ReservaProdutoForms(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso!')
            return redirect('reservas')
    return render(request, 'reservas/_editar_reservas.html', {"form": form, 'produtos': produto})

def editar_reserva_servico(request,id):
    servico = ReservaServico.objects.get(pk=id)
    form = ReservaServicoForms(instance=servico)

    if request.method == 'POST':
        form = ReservaServicoForms(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa editada com sucesso!')
            return redirect('reservas')
    return render(request, 'reservas/_editar_reservas.html', {"form": form, 'servicos': servico})

def deletar_reserva_produto(request, id):
    reserva = ReservaProduto.objects.get(id=id)
    reserva.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('reservas')

def deletar_reserva_servico(request, id):
    reserva = ReservaServico.objects.get(id=id)
    reserva.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('reservas')

def nova_reserva_servico(request, id):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect("login")
    
    servico = Servico.objects.get(id=id)  # Obtém o serviço pelo ID

    if request.method == "POST":
        form = ReservaServicoForms(request.POST, servico)  # Passa o serviço para o formulário
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.servico = servico  # Garante que o serviço será associado à reserva
            reserva.user = request.user  # Atribui o usuário logado à reserva
            reserva.save()
            messages.success(request, "Nova Reserva de Serviço cadastrada!")
            return redirect("index")
    else:
        form = ReservaServicoForms
    
    return render(request, 'reservas/_criar_reserva.html', {"form": form, "servico": servico})