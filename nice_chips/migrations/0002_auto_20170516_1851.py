# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nice_chips', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyDraft',
            new_name='Draft',
        ),
    ]
