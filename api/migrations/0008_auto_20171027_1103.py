# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171026_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='priority',
            field=models.IntegerField(default=3),
        ),
    ]