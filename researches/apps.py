from django.apps import AppConfig
from django.db.models.signals import post_delete, pre_save

class ResearchesConfig(AppConfig):
    name = 'researches'
    verbose_name='pesquisas'

    def ready(self):
        from .models import Publication
        from .signals import delete_article, delete_old_article

        post_delete.connect(delete_article, sender=Publication)
        pre_save.connect(delete_old_article, sender=Publication)
