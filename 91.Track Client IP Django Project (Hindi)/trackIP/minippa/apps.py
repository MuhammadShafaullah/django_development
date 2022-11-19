from django.apps import AppConfig


class MinippaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'minippa'
    
    def ready(self):
        import minippa.singnals
