# Generated by Django 2.2.13 on 2020-07-06 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_openreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
