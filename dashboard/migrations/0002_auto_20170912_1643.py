# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dietary_restrictions',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]