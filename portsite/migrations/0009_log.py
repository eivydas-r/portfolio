# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-08-10 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portsite', '0008_auto_20200810_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
            ],
        ),
    ]