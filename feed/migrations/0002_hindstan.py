# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hindstan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
