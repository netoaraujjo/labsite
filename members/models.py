# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Member(models.Model):
    MEMBER_CATEGORIES = (
        ('1', 'Orientador'),
        ('2', 'Mestrando'),
        ('3', 'Graduando'),
    )

    category = models.CharField(
        max_length=1,
        choices=MEMBER_CATEGORIES,
        verbose_name='categoria',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='nome',
    )
    email = models.EmailField(verbose_name='e-mail')
    lattes = models.URLField(verbose_name='currículo Lattes')
    avatar = models.FileField(upload_to='uploads/pictures/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Membro'
