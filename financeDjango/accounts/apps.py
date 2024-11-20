from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'financeDjango.accounts'

    def ready(self):
        import financeDjango.accounts.signals