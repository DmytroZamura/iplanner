# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_projectteam'),
    ]

    operations = [




        migrations.AlterField(
            model_name='projectfile',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
