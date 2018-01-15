# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_timeupdated'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]