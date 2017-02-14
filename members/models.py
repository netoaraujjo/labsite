# -*- coding:utf-8 -*-
from django.db import models





# def update_filename(instance, filename):
#     path = "upload/path/"
#     format = instance.userid + instance.transaction_uuid + instance.file_extension
#     return os.path.join(path, format)

# file = models.FileField(
#     upload_to=lambda instance, filename: '/'.join(['mymodel', str(instance.pk), filename]),
# )





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
        return ('%s,%s') % (self.latitude, self.longitude)

    class Meta:
        verbose_name='localização'
        verbose_name_plural='localizações'


class AboutLab(models.Model):
    lab_name = models.CharField(
        max_length=200,
        verbose_name='nome do laboratório',
    )
    about = models.TextField(verbose_name='sobre')
    image = models.ImageField(
        upload_to='about',
        verbose_name='imagem',
    )

    def __str__(self):
        return self.lab_name

    class Meta():
        verbose_name='sobre'
        verbose_name_plural='sobre'
