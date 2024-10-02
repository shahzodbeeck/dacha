from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Province(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PopularPlaces(models.Model):
    name = models.CharField(max_length=100, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_regions(sender, **kwargs):
    from regions.lists import provinces_data,districts_data
    for province in provinces_data:
        Province.objects.get_or_create(
            name_uz=province['name_uz'],
            name_ru=province['name_ru'],
            name_en=province['name_en']
        )

    for district in districts_data:
        District.objects.get_or_create(
            name_uz=district['name_uz'],
            name_ru=district['name_ru'],
            name_en=district['name_en'],
            province_id=district['province_id']
        )
