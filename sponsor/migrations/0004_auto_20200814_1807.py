# Generated by Django 2.2.13 on 2020-08-14 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sponsor', '0003_auto_20200709_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='manager_id',
            field=models.ForeignKey(blank=True, help_text='후원사를 위한 추가 아이디', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_temp_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='creator',
            field=models.ForeignKey(help_text='후원사를 등록한 유저', on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
