from django.urls import path
from apps.produtos.views import index,novo_produto,produto,info_produto

urlpatterns = [
    path('', index, name='index'),
    path('novo-produto/', novo_produto, name='novo-produto'),
    path('produtos/', produto, name='produto'),
    path('produtos/<int:id>', info_produto, name='info-produto'),
]
