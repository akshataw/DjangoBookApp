# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='book_number',
        ),
    ]
