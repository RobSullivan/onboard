# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_route', models.CharField(max_length=7)),
                ('bus_stop', models.CharField(max_length=5)),
            ],
        ),
    ]