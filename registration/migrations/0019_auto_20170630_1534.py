# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20170619_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='top_size',
            field=models.CharField(blank=True, choices=[('small', 'S(85)'), ('medium', 'M(90)'), ('large', 'L(95)'), ('xlarge', 'XL(100)'), ('2xlarge', '2XL(105)'), ('3xlarge', '3XL(110)'), ('4xlarge', '4XL(115)')], default=None, max_length=20, null=True),
        ),
    ]