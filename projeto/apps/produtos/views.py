from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from apps.produtos.forms import ProdutoForm
from apps.produtos.models import Produto
from apps.servicos.models import Servico

def index(request):
    # if not request.user.is_authenticated:
    #     messages.success(request, "Usuário não logado!")
    #     return redirect('login')
    produtos = Produto.objects.order_by("nome")
    servicos = Servico.objects.order_by('nome')
    return render(request, 'produtos/index.html', {"produtos": produtos, 'servicos': servicos})

def produto(request):
    produtos = Produto.objects.order_by("nome")
    return render(request, 'produtos/_produtos.html', {"produtos": produtos})

def info_produto(request,id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'produtos/_informacao_produto.html', {"produtos": produto})
    
def novo_produto(request):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    
    #produto = get_object_or_404(Produto, id=id)
    
    #empresa = produto.empresa
    if request.method == 'POST':
        form = ProdutoForm(request.POST)  # Passa o produto para o formulário
        if form.is_valid():
            form.save()  
            messages.success(request, 'Nova Venda cadastrada!')
            return redirect('index')

    form = ProdutoForm
    return render(request, 'produtos/_criar_produto.html', {'form': form})

def editar_produto(request,id):
    produto = Produto.objects.get(pk=id)
    form = ProdutoForm(instance=produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editada com sucesso!')
            return redirect('reservas')
    return render(request, 'produtos/_editar_produto.html', {"form": form, 'produtos': produto})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('produto')