# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_auto_20171013_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menus/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shops/%Y/%m/%d/'),
        ),
    ]