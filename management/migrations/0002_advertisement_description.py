# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
