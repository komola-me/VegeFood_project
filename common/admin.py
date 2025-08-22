from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from common.models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)