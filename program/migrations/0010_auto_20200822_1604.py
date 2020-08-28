# Generated by Django 2.2.13 on 2020-08-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0009_proposal_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='slide_url',
            field=models.CharField(blank=True, help_text='발표 자료 URL', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='video_open_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='video_url',
            field=models.CharField(blank=True, help_text='발표 영상 URL', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='introduction',
            field=models.TextField(blank=True, help_text='발표 소개 페이지에 들어가는 내용입니다.', max_length=1000, null=True),
        ),
    ]