from modeltranslation import translator

from .models import Product, ProductCategory, ProductVariant

@translator.register(Product)
class ProductTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'description', 'price', 'image', 'category', 'is_featured', 'created_at', 'updated_at',)


@translator.register(ProductCategory)
class ProductCategoryTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'description', 'image', 'is_active', 'sort_order',)


@translator.register(ProductVariant)
class ProductVariantTranslationOptions(translator.TranslationOptions):
    fields = ('product', 'name', 'price', 'color', 'size',)