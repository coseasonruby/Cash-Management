# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-05 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemo', '0020_auto_20180531_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash_post',
            name='a_r_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cash_post',
            name='collection_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cash_post',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
