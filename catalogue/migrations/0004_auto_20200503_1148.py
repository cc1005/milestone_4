# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-03 11:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_fulldocument_document_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fulldocument',
            old_name='document_catalogue',
            new_name='catalogue',
        ),
    ]