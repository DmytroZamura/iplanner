# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 17:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0009_auto_20170922_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMockup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField()),
                ('accepted_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('accepted_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mockup_versions', to='project.Project')),
            ],
            options={
                'ordering': ['project', '-version'],
            },
        ),
        migrations.CreateModel(
            name='ProjectMockupFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('project_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectFile')),
                ('project_mockup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectMockup')),
            ],
        ),
    ]
