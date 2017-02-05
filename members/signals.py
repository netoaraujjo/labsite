def delete_photo(sender, instance, **kwargs):
    instance.avatar.delete(False)
