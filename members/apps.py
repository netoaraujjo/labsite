# -*- coding:utf-8 -*-
from django.apps import AppConfig
from django.db.models.signals import post_delete, pre_save

class MembersConfig(AppConfig):
    name = 'members'
    verbose_name = 'Laboratório'

    def ready(self):
        from .models import Member
        from .signals import delete_photo, delete_old_photo

        post_delete.connect(delete_photo, sender=Member)
        pre_save.connect(delete_old_photo, sender=Member)
