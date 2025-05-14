from django.apps import AppConfig


class AdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ads'
    # def ready(self):
    #     # Проверяем и создаём БД при старте Django
    #     from ads.ensure_db import ensure_db_exists
    #     ensure_db_exists()