# -*- coding:utf-8 -*-
from django.db import models

from members.models import Member

# Create your models here.
class ResearchLine(models.Model):
    research_line = models.CharField(
        max_length=200,
        verbose_name='linha de pesquisa',
    )
    description = models.TextField(
        max_length=1024,
        verbose_name='descrição',
    )
    image = models.ImageField(
        upload_to='research_lines',
        verbose_name='imagem',
    )

    def __str__(self):
        return self.research_line

    class Meta:
        verbose_name='linha de pesquisa'
        verbose_name_plural='linhas de pesquisa'


class Publication(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='título',
    )
    publication_local=models.CharField(
        max_length=200,
        verbose_name='local de publicação',
        help_text='Congresso/Periódico onde o artigo foi publicado.',
    )
    publication_url = models.URLField(
        verbose_name='link da publicação',
    )
    authors = models.ManyToManyField(
        Member,
        related_name='publications',
        verbose_name='autores',
        help_text='Autores vinculados ao laboratório.',
    )
    publication_file=models.FileField(
        upload_to='publications',
        verbose_name='',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='publicação'
        verbose_name_plural='Publicações'
