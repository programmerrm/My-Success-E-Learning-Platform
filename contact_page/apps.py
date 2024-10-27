from django.apps import AppConfig

class ContactPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_page'

    def ready(self):
        import contact_page.signals