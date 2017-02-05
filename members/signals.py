from .models import Member

def delete_photo(sender, instance, **kwargs):
    instance.avatar.delete(False)

def delete_old_photo(sender, instance, **kwargs):
    if instance.id:
        member = Member.objects.get(id=instance.id)
        if member.avatar:
            member.avatar.delete(False)
