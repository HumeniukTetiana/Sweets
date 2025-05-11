from django.apps import AppConfig


class ConcurrentDbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'concurrent_db'
