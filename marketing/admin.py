from django.contrib import admin
from . import models


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("order", "short_q", "short_a")
