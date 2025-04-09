from django.shortcuts import render,get_object_or_404,redirect
from apps.servicos.models import Servico
from django.contrib import messages
from apps.servicos.forms import ServicoForm

def servico(request):
    servicos = Servico.objects.order_by("nome")
    return render(request, 'servicos/_servicos.html', {"servicos": servicos})

def info_servico(request,id):
    servico = get_object_or_404(Servico, pk=id)
    return render(request, 'servicos/_informacao_servico.html', {"servicos": servico})

def novo_servico(request):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    if not request.user.is_staff:
        messages.error(request, "Você não tem permissão para acessar essa funcionalidade.")
        return redirect('index')  # ou qualquer outra view mais apropriada
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES)  # Passa o produto para o formulário
        if form.is_valid():
            form.save()  
            messages.success(request, 'Novo serviço cadastrado!')
            return redirect('servico')

    form = ServicoForm()
    return render(request, 'servicos/_criar_servico.html', {'form': form})

def editar_servico(request,id):
    servico = Servico.objects.get(pk=id)
    form = ServicoForm(instance=servico)

    if request.method == 'POST':
        form = ServicoForm(request.POST,request.FILES, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'servico editada com sucesso!')
            return redirect('reservas')
    return render(request, 'servicos/_editar_servico.html', {"form": form, 'servicos': servico})

def deletar_servico(request, id):
    servico = Servico.objects.get(id=id)
    servico.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('servico')