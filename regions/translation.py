from modeltranslation.translator import register, TranslationOptions

from .models import Province, District, PopularPlaces


@register(Province)
class ProvinceTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PopularPlaces)
class PopularPlacesTranslationOptions(TranslationOptions):
    fields = ('name',)
