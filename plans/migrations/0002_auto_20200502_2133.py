# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-02 21:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FirnessPlan',
            new_name='PremiumPlan',
        ),
    ]
