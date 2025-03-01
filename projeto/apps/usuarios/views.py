from django.shortcuts import render

def login(request):
    #reserva = Reserva.objects.order_by("id")
    return render(request, 'usuarios/login.html')#, {"cards": reserva})
