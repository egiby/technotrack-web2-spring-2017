from django.apps import AppConfig


class UsgConfig(AppConfig):
    name = 'ugc'

    def ready(self):
        from ugc import signals
