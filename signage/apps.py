from django.apps import AppConfig


class SignageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signage'

    def ready(self):
        super().ready()
        from . import signals


