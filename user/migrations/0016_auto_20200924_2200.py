# Generated by Django 2.2.13 on 2020-09-24 13:00

from django.db import migrations
import sorl.thumbnail.fields
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20200924_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_ori',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='사용자 사진 원본', null=True, upload_to=user.models.profile_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_small',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='사용자 사진 축소본', null=True, upload_to=user.models.profile_image),
        ),
    ]
