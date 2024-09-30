from django.db import models
from deep_translator import GoogleTranslator


class Plan(models.Model):
    name_uz = models.CharField(max_length=100, blank=True)
    name_en = models.CharField(max_length=100, blank=True)
    name_ru = models.CharField(max_length=100, blank=True)

    description_uz = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)

    price = models.FloatField()
    duration = models.IntegerField()

    def save(self, *args, **kwargs):
        translator = GoogleTranslator()

        if self.name_en:
            if not self.name_uz:
                self.name_uz = translator.translate(self.name_en, target='uz')
            if not self.name_ru:
                self.name_ru = translator.translate(self.name_en, target='ru')
        elif self.name_uz:
            if not self.name_en:
                self.name_en = translator.translate(self.name_uz, target='en')
            if not self.name_ru:
                self.name_ru = translator.translate(self.name_uz, target='ru')
        elif self.name_ru:
            if not self.name_en:
                self.name_en = translator.translate(self.name_ru, target='en')
            if not self.name_uz:
                self.name_uz = translator.translate(self.name_ru, target='uz')

        if self.description_en:
            if not self.description_uz:
                self.description_uz = translator.translate(self.description_en, target='uz')
            if not self.description_ru:
                self.description_ru = translator.translate(self.description_en, target='ru')
        elif self.description_uz:
            if not self.description_en:
                self.description_en = translator.translate(self.description_uz, target='en')
            if not self.description_ru:
                self.description_ru = translator.translate(self.description_uz, target='ru')
        elif self.description_ru:
            if not self.description_en:
                self.description_en = translator.translate(self.description_ru, target='en')
            if not self.description_uz:
                self.description_uz = translator.translate(self.description_ru, target='uz')

        super(Plan, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en
