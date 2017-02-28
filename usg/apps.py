from django.apps import AppConfig


class UsgConfig(AppConfig):
    name = 'usg'

    def ready(self):
        from usg import signals
