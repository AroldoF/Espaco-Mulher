from django.shortcuts import render

def calendario(request):
    #reserva = Reserva.objects.order_by("id")
    return render(request, 'reservas/calendario.html')#, {"cards": reserva})