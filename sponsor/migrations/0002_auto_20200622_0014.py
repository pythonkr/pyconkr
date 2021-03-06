# Generated by Django 2.2.10 on 2020-06-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='virtual_booth_content_en',
            field=models.TextField(blank=True, help_text='Virtual booth에 들어가는 내용입니다. 홈페이지의 virtual booth에 게시됩니다.', null=True),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='virtual_booth_content_ko',
            field=models.TextField(blank=True, help_text='Virtual booth에 들어가는 내용입니다. 홈페이지의 virtual booth에 게시됩니다.', null=True),
        ),
    ]
