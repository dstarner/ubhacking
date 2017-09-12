from django.shortcuts import render
from . import models


def index(request):
    faqs = models.FAQ.objects.all()
    return render(request, "marketing/index.html", {"faqs": faqs})
