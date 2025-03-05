from django.shortcuts import render,redirect

from apps.usuarios.forms import LoginForms,CadastroForms

from apps.reservas.models import ReservaProduto,ReservaServico

from django.contrib.auth.models import User

from django.contrib import auth,messages

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form["nome_login"].value()
            senha=form["senha"].value()

        usuario=auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Erro ao efetuar login!")
            return redirect('login')


    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, f"User {nome} já existente")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

@login_required
def gerenciar(request):
    reservas_produtos = ReservaProduto.objects.filter(user=request.user, disponivel=False)
    reservas_servicos = ReservaServico.objects.filter(user=request.user, disponivel=False)

    return render(request, "usuarios/_gerenciar.html", {
        "reservas_produtos": reservas_produtos,
        "reservas_servicos": reservas_servicos,
    })

@login_required
def atualizar_disponibilidade(request):
    if request.method == "POST":
        tipo = request.POST.get("tipo")
        reserva_id = request.POST.get("id")

        if tipo == "produto":
            reserva = ReservaProduto.objects.filter(id=reserva_id).first()
        elif tipo == "servico":
            reserva = ReservaServico.objects.filter(id=reserva_id).first()
        else:
            return JsonResponse({"success": False, "message": "Tipo inválido"}, status=400)

        if reserva:
            reserva.disponivel = True
            reserva.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "message": "Reserva não encontrada"}, status=404)

    return JsonResponse({"success": False, "message": "Método inválido"}, status=400)
