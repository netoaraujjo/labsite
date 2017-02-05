from .models import Publication

def delete_article(sender, instance, **kwargs):
    instance.publication_file.delete(False)

def delete_old_article(sender, instance, raw, **kwargs):
    if instance.id:
        publication = Publication.objects.get(id=instance.id)
        publication.publication_file.delete(False)
