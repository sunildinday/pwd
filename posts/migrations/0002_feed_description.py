# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 05:37
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]