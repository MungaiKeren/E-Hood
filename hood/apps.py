from django.apps import AppConfig


class HoodConfig(AppConfig):
    name = 'hood'

    def ready(self):
        import hood.signals
