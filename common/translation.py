from modeltranslation import translator

from .models import BaseModel, Sponsor

# @translator.register(BaseModel)
# class BaseModelTranslationOptions(translator.TranslationOptions):
#     fields = ('created_at', 'updated_at',)


@translator.register(Sponsor)
class SponsorTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'logo',)