from django.urls import path
from apps.usuarios.views import login,cadastro,logout,gerenciar,atualizar_disponibilidade

urlpatterns=[
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path("gerenciar/", gerenciar, name="gerenciar"),
    path("atualizar-disponibilidade/", atualizar_disponibilidade, name="atualizar_disponibilidade"),
]