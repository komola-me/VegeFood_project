from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    phone_number = models.CharField(
        _("Phone Number"), max_length=20, null=True, blank=True
    )
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Last Name"))
    profession = models.ForeignKey(
        "users.Profession",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="users",
        verbose_name=_("Profession")
    )
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name=_("Avatar"))
    favourites = models.ManyToManyField(
        "products.ProductVariant",
        through="UserFavorites",
        through_fields=("user", "product_variant"),
        related_name="favourite_users",
        verbose_name=_("favourites")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_confirmed = models.BooleanField(default=False, verbose_name=_("Is Confirmed"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Is Staff"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Is Superuser"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email


class Profession(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Profession")
        verbose_name_plural = _("Professions")


class Cart(BaseModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="cart",
        verbose_name=_("User")
    )

    def __str__(self):
        return f"{self.user}"

    def get_subtotal(self):
        return sum(item.get_unit_price() * item.quantity for item in self.items.all())

    def get_discount_total(self):
        return self.get_subtotal() - sum(item.get_total_price() for item in self.items.all())

    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        if self.applied_promo:
            total = self.applied_promo.apply_discount(total)
        return total

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(BaseModel):
    cart = models.ForeignKey(
        "users.Cart", on_delete=models.CASCADE, related_name="cart_items",
        verbose_name=_("cart")
    )
    product = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE, related_name="cart_items",
        verbose_name=_("product")
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("quantity"))

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    def get_unit_price(self):
        return self.product.price

    def get_discounted_price(self):
        discount = self.product.get_active_discount()
        if not discount:
            return self.get_unit_price()

        if discount.discount_type == "PERCENT":
            return self.get_unit_price() * (100 - discount.value) / 100
        elif discount.discount_type == "FIXED":
            return max(0, self.get_unit_price() - discount.value)
        return self.get_unit_price()

    def get_total_price(self):
        return self.get_discounted_price() * self.quantity

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")


class UserFavorites(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name=_("User"))
    product_variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE, verbose_name=_("Product Variant")
    )

    def __str__(self):
        return f"{self.user} - {self.product_variant}"

    class Meta:
        verbose_name = _("User Favorite")
        verbose_name_plural = _("User Favorites")
        unique_together = ("user", "product_variant")


class UserFeedback(BaseModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="feedbacks", verbose_name=_("user")
    )
    message = models.CharField(max_length=500, verbose_name=_("message"))

    def __str__(self):
        return f"{self.user} - {self.message}"

    class Meta:
        verbose_name = _("User Feedback")
        verbose_name_plural = _("User Feedbacks")