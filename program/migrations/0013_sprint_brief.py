# Generated by Django 2.2.13 on 2020-08-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0012_sprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='brief',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
