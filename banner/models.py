from django.db import models


class Banners(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')
