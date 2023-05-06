from django.apps import AppConfig

class AccountConfig(AppConfig):
    name='account'

    def ready(self) -> None:
        from .task import start
        start()