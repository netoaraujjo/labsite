# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Member(models.Model):
    MEMBER_CATEGORIES = (
        ('Orientador', 'Orientador'),
        ('Mestrando', 'Mestrando'),
        ('Graduando', 'Graduando'),
    )

    category = models.CharField(
        max_length=30,
        choices=MEMBER_CATEGORIES,
        verbose_name='categoria',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='nome',
    )
    email = models.EmailField(verbose_name='e-mail')
    lattes = models.URLField(verbose_name='currículo Lattes')
    avatar = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Membro'


class Location(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    google_maps_api_key=models.CharField(
        max_length=200,
        verbose_name='API Key do Google Maps'
    )
    address = models.TextField(
        max_length=200,
        verbose_name='endereço',
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name='localização'
        verbose_name_plural='localizações'


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='título',
    )
    text = models.TextField(
        verbose_name='texto',
    )
    image = models.ImageField(
        upload_to='posts',
        verbose_name='imagem',
    )
    pub_date = models.DateTimeField(
        verbose_name='data de publicação',
    )

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'notícia'
