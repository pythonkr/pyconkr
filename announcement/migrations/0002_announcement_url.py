# Generated by Django 2.2.10 on 2020-05-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='url',
            field=models.URLField(default='https://ko-kr.facebook.com/pyconkorea/', max_length=500),
            preserve_default=False,
        ),
    ]
