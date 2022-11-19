from django.apps import AppConfig


class JangosignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jangoSignal'
    
    def ready(self):
        import jangoSignal.signals
