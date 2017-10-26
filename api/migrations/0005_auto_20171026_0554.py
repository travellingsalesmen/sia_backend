# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171025_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawSpareDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('drawn', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='NewDefect',
            new_name='RawDefect',
        ),
        migrations.RemoveField(
            model_name='newsparedetail',
            name='newDefect',
        ),
        migrations.RemoveField(
            model_name='newsparedetail',
            name='spare',
        ),
        migrations.AlterField(
            model_name='defect',
            name='techsAssigned',
            field=models.ManyToManyField(blank=True, related_name='defectsAssigned', to='api.Profile'),
        ),
        migrations.DeleteModel(
            name='NewSpareDetail',
        ),
        migrations.AddField(
            model_name='rawsparedetail',
            name='rawDefect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spares', to='api.RawDefect'),
        ),
        migrations.AddField(
            model_name='rawsparedetail',
            name='spare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rawUses', to='api.Spare'),
        ),
    ]
