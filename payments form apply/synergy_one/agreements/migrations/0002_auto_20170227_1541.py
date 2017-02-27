# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-27 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='agreement',
        ),
        migrations.RenameField(
            model_name='agreement',
            old_name='_id',
            new_name='external_id',
        ),
        migrations.AddField(
            model_name='agreement',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]