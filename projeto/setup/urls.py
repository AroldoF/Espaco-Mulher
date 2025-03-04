from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('setup.api.urls')),
    path('', include('apps.reservas.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.produtos.urls')),
]
