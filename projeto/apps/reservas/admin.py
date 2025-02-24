from django.contrib import admin
from apps.reservas.models import ReservaProduto, ReservaServico

class ReservasProdutos(admin.ModelAdmin):
    list_display = ('id','produto','user','quantidade_comprada','valor_total','data_reservada','disponivel')
    list_display_links = ('id','produto','user')
    list_per_page = 10
    search_fields= ('produto','user','data_reservada')
    ordering = ('id','produto','user','data_reservada')

admin.site.register(ReservaProduto,ReservasProdutos)

class ReservasServicos(admin.ModelAdmin):
    list_display = ('id','servico','user','valor_total','data_reservada','disponivel')
    list_display_links = ('id','servico','user')
    list_per_page = 10
    search_fields= ('servico','user','data_reservada')
    ordering = ('id','servico','user','data_reservada')

admin.site.register(ReservaServico,ReservasServicos)