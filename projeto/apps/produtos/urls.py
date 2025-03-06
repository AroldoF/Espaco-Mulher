from django.urls import path
from apps.produtos.views import index,novo_produto,produto,info_produto,editar_produto,deletar_produto

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', produto, name='produto'),
    path('produtos/<int:id>', info_produto, name='info-produto'),
    path('novo-produto/', novo_produto, name='novo-produto'),
    path('editar-produtos/<int:id>', editar_produto, name='editar-produtos'),
    path('deletar-produtos/<int:id>', deletar_produto, name='deletar-produtos'),
]
