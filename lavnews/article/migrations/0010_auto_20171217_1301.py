# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20171217_1259'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='azaza',
            new_name='Blog_Settings',
        ),
        migrations.RenameField(
            model_name='blog_settings',
            old_name='azaza_title',
            new_name='Blog_Settings_title',
        ),
        migrations.AlterModelTable(
            name='blog_settings',
            table='Blog_Settings',
        ),
    ]
