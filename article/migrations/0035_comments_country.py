# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0034_auto_20190508_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
