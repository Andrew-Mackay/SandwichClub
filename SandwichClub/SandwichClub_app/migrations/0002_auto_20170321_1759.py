# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SandwichClub_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='picture',
            field=models.ImageField(upload_to='sandwich_images'),
        ),
        migrations.AlterField(
            model_name='sandwich',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]