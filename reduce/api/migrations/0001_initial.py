# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20171008_1015'),
        ('owner', '0006_auto_20171013_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=128)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Customer')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Shop')),
            ],
        ),
    ]