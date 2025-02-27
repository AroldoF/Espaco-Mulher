from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.produtos.api.views import ProdutoViewSet
from apps.servicos.api.views import ServicoViewSet
from apps.usuarios.api.views import UserViewSet
from apps.reservas.api.views import ReservaProdutoViewSet,ReservaServicoViewSet


router = DefaultRouter()
router.register('produtos', ProdutoViewSet, basename='produto')
router.register('servicos', ServicoViewSet, basename='servico')
router.register('usuarios', UserViewSet, basename='usuario')
router.register('reservas-produtos', ReservaProdutoViewSet, basename='reserva-produto')
router.register('reservas-servicos', ReservaServicoViewSet, basename='reserva-servico')

urlpatterns = [
    path('', include(router.urls)),  # Aqui será a raiz da API
    # path('reservas/', include('apps.reservas.api.urls')),
]
