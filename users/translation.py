from modeltranslation import translator

from .models import User, UserFavorites, UserFeedback, Cart, CartItem, Profession

@translator.register(User)
class UserTranslationOptions(translator.TranslationOptions):
    fields = ('first_name', 'last_name',)


@translator.register(UserFeedback)
class UserFeedbackTranslationOptions(translator.TranslationOptions):
    fields = ('message',)


@translator.register(Profession)
class ProfessionTranslationOptions(translator.TranslationOptions):
    fields = ('name',)