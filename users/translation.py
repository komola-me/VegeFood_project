from modeltranslation import translator

from .models import User, UserFavorites, UserFeedback, Cart, CartItem, Profession

@translator.register(User)
class UserTranslationOptions(translator.TranslationOptions):
    fields = ('email', 'phone_number', 'first_name', 'last_name', 'profession', 'avatar', 'favourites', 'is_active', 'is_confirmed', 'is_staff', 'is_superuser',)


@translator.register(UserFavorites)
class UserFavoritesTranslationOptions(translator.TranslationOptions):
    fields = ()


@translator.register(UserFeedback)
class UserFeedbackTranslationOptions(translator.TranslationOptions):
    fields = ()


@translator.register(Profession)
class ProfessionTranslationOptions(translator.TranslationOptions):
    fields = ('name',)


@translator.register(Cart)
class CartTranslationOptions(translator.TranslationOptions):
    fields = ('user',)


@translator.register(CartItem)
class CartItemTranslationOptions(translator.TranslationOptions):
    fields = ('cart', 'product', 'quantity',)