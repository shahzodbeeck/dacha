from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryServices(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
