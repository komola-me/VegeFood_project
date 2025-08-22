from modeltranslation import translator

from .models import Provider, PromocodeUsage, ProductDiscount, Promocode, Discount, ProductDiscount, Order, OrderItem, OrderStatus, Transaction, TransactionStatus

@translator.register(Order)
class OrderTranslationOptions(translator.TranslationOptions):
    fields = ('user', 'promocode', 'total_amount', 'status', 'notes', 'ordered_at', 'purchased_at',)


@translator.register(OrderItem)
class OrderItemTranslationOptions(translator.TranslationOptions):
    fields = ('order', 'product', 'quantity', 'price')


@translator.register(Provider)
class ProviderTranslationOptions(translator.TranslationOptions):
    fields = ('name',)


@translator.register(Transaction)
class TransactionTranslationOptions(translator.TranslationOptions):
    fields = ('order', 'provider', 'status', 'paid_at', 'cancelled_at', 'amount',)


@translator.register(Discount)
class DiscountTranslationOptions(translator.TranslationOptions):
    fields = ('title', 'description', 'discount_type', 'value', 'is_active',)


@translator.register(ProductDiscount)
class ProductDiscountTranslationOptions(translator.TranslationOptions):
    fields = ('product', 'discount', 'valid_from', 'valid_until',)


@translator.register(Promocode)
class PromocodeTranslationOptions(translator.TranslationOptions):
    fields = ('code', 'description', 'type', 'value', 'min_amount', 'usage_limit', 'valid_from', 'valid_until', 'is_active',)


@translator.register(PromocodeUsage)
class PromodcodeUsageTranslationOptions(translator.TranslationOptions):
    fields = ('promocode_id', 'used_at')
