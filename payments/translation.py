from modeltranslation import translator

from .models import Provider, ProductDiscount, Promocode, Discount, ProductDiscount, Order, OrderItem, OrderStatus, Transaction, TransactionStatus

@translator.register(Order)
class OrderTranslationOptions(translator.TranslationOptions):
    fields = ('status', 'notes',)


@translator.register(Provider)
class ProviderTranslationOptions(translator.TranslationOptions):
    fields = ('name',)


@translator.register(Transaction)
class TransactionTranslationOptions(translator.TranslationOptions):
    fields = ('status', 'amount',)


@translator.register(Discount)
class DiscountTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'description', 'discount_type',)


@translator.register(Promocode)
class PromocodeTranslationOptions(translator.TranslationOptions):
    fields = ('code', 'description', 'type',)