from django.apps import AppConfig
from django.db.models.signals import post_delete

class ResearchesConfig(AppConfig):
    name = 'researches'
    verbose_name='pesquisas'

    def ready(self):
        from .models import Publication
        from .signals import delete_article

        post_delete.connect(delete_article, sender=Publication)
