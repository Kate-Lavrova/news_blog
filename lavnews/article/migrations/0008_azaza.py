# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_delete_azaza'),
    ]

    operations = [
        migrations.CreateModel(
            name='azaza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azaza_title', models.CharField(default='azaaza', max_length=200)),
            ],
            options={
                'db_table': 'azaza',
            },
        ),
    ]