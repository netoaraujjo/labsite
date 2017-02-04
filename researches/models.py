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

    def __str__(self):
        return self.research_line

    class Meta:
        verbose_name='linha de pesquisa'
        verbose_name_plural='linhas de pesquisa'


class Project(models.Model):
    researches = models.ManyToManyField(
        Member,
        related_name='projects',
        verbose_name='Pesquisadores',
    )
    research_line = models.ForeignKey(
        ResearchLine,
        on_delete=models.CASCADE,
        verbose_name='linha de pesquisa',
        default=1,
    )
    project_title = models.CharField(
        max_length=200,
        verbose_name='título',
    )
    abstract = models.TextField(
        max_length=1024,
        verbose_name='resumo',
    )

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name='projeto'
