# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-04 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fulldocument',
            name='catalogue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogue', to='catalogue.Catalogue'),
        ),
    ]