from django.shortcuts import render, redirect
from django.contrib import messages
from apps.produtos.models import Produto
from apps.servicos.models import Servico

def index(request):
    # if not request.user.is_authenticated:
    #     messages.success(request, "Usuário não logado!")
    #     return redirect('login')
    produtos = Produto.objects.order_by("nome")
    servicos = Servico.objects.order_by('nome')
    return render(request, 'produtos/index.html', {"produtos": produtos, 'servicos': servicos})
