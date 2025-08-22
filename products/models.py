from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    image = models.ImageField(upload_to="products", verbose_name=_("image"))
    category = models.ForeignKey(
        "products.ProductCategory", on_delete=models.RESTRICT, related_name="products", verbose_name=_("category")
    )
    is_featured = models.BooleanField(default=False, verbose_name=_("Is Featured"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductVariant(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.RESTRICT, related_name="variants", verbose_name=_("Product")
    )
    name = models.CharField(max_length=255, verbose_name=_("name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    color = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("color"))
    size = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("size"))

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")


class ProductCategory(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name=_("name"))
    description = models.CharField(max_length=500, blank=True, verbose_name=_("description"))
    image = models.ImageField(upload_to="categories/", blank=True, null=True, verbose_name=_("image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    sort_order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Sort Order"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name