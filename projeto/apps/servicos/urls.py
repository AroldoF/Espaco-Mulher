from django.urls import path
from apps.servicos.views import servico,info_servico,novo_servico,editar_servico,deletar_servico

urlpatterns = [
    path('servicos/', servico, name='servico'),
    path('servicos/<int:id>', info_servico, name='info-servico'),
    path('novo-servico/', novo_servico, name='novo-servico'),
    path('editar-servicos/<int:id>', editar_servico, name='editar-servico'),
    path('deletar-servicos/<int:id>', deletar_servico, name='deletar-servico'),
]
