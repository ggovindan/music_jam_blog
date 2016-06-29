# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 01:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vblog', '0005_auto_20160627_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('event_date', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
    ]
