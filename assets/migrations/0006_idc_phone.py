# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-15 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20170315_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='idc',
            name='phone',
            field=models.CharField(default=13155356666L, max_length=255, verbose_name='\u8054\u7cfb\u7535\u8bdd'),
            preserve_default=False,
        ),
    ]
