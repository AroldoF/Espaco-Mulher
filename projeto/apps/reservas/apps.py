from django.apps import AppConfig


class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reservas'
    
    def ready(self):
        import apps.reservas.signals  # Importa os signals ao iniciar o app