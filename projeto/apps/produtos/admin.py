from django.contrib import admin
from apps.produtos.models import Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id','nome','descricao','preco','estoque',)
    list_display_links = ('id','nome',)
    list_per_page = 10
    search_fields= ('nome',)
    ordering = ('nome','preco',)

admin.site.register(Produto,Produtos)