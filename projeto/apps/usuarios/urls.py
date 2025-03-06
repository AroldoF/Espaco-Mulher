from django.urls import path
from apps.usuarios.views import login,cadastro,logout,gerenciar,atualizar_disponibilidade,gerenciar_produtos

urlpatterns=[
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path("gerenciar-reservas/", gerenciar, name="gerenciar"),
    path("gerenciar-produtos/", gerenciar_produtos, name="gerenciar-produtos"),
    path("atualizar-disponibilidade/", atualizar_disponibilidade, name="atualizar_disponibilidade"),
]