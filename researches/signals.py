def delete_article(sender, instance, **kwargs):
    instance.publication_file.delete(False)
