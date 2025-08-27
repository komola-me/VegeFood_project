from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

from users.models import Profession, UserFeedback, UserFavorites, User


@admin.register(User)
class UserAdmin(TranslationAdmin, BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_display_links = ["id", "email"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["id"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


@admin.register(Profession)
class ProfessionAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


@admin.register(UserFeedback)
class UserFeedbackAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ["id", "user", "message"]
    list_display_links = ["id", "user"]
    search_fields = ["user"]


@admin.register(UserFavorites)
class UserFavoritesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product_variant']
    list_display_links = ['id', 'user', 'product_variant']
    search_fields = ['user']