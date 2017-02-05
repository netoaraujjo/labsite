# -*- coding:utf-8 -*-
from django.apps import AppConfig
from django.db.models.signals import post_delete

class MembersConfig(AppConfig):
    name = 'members'
    verbose_name = 'Laboratório'

    def ready(self):
        from .models import Member
        from .signals import delete_photo

        post_delete.connect(delete_photo, sender=Member)
