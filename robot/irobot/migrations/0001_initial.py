# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-01-29 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100000)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
