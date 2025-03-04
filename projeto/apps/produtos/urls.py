from django.urls import path
from apps.produtos.views import index

urlpatterns = [
    path('', index, name='index'),
]
