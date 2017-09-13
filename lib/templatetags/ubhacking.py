import os

from django import template


register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

@register.filter
def can_change_acception(status):
    return status in ["Accepted", "Attending", "Declined"]
