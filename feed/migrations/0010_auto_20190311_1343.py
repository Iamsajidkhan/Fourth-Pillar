# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-11 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_indextop10_frequency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indextop10',
            old_name='frequency',
            new_name='db_frequency',
        ),
        migrations.RenameField(
            model_name='indextop10',
            old_name='keyword',
            new_name='db_keyword',
        ),
    ]
