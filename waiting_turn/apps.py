from django.apps import AppConfig


class WaitingTurnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'waiting_turn'
    def ready(self):
        import waiting_turn.signals
