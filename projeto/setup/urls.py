from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Documentação da API de Empresas - Tilha Nadic",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aroldo.caval@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('setup.api.urls')),
    path('', include('apps.reservas.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.produtos.urls')),
    path('', include('apps.servicos.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
