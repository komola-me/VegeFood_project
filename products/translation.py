from modeltranslation import translator

from .models import Product, ProductCategory, ProductVariant

@translator.register(Product)
class ProductTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'description',)


@translator.register(ProductCategory)
class ProductCategoryTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'description', 'sort_order',)


@translator.register(ProductVariant)
class ProductVariantTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'color', 'size',)