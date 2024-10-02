from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField()
    duration = models.IntegerField()
