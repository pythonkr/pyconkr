# Generated by Django 2.2.10 on 2020-06-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_auto_20200618_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='virtual_hall_content',
            field=models.TextField(blank=True, help_text='Virtual booth에 들어가는 내용입니다. 홈페이지의 virtual booth에 게시됩니다.', null=True),
        ),
    ]