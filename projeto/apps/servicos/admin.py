from django.contrib import admin
from apps.servicos.models import Servico

class Servicos(admin.ModelAdmin):
    list_display = ('id','nome','descricao','preco','tempo_duracao')
    list_display_links = ('id','nome',)
    list_per_page = 10
    search_fields= ('nome',)
    ordering = ('nome','preco',)

admin.site.register(Servico,Servicos)