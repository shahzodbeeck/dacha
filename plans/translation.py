from modeltranslation.translator import register, TranslationOptions

from .models import Plan


@register(Plan)
class PlanTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
