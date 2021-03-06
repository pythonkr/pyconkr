# Generated by Django 2.2.13 on 2020-07-14 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0003_auto_20200706_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='openreview',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='program.ProgramCategory'),
        ),
        migrations.AddField(
            model_name='openreview',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='LightningTalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='라이트닝 토크 제목', max_length=255, null=True)),
                ('slide_url', models.CharField(max_length=511, null=True)),
                ('day', models.IntegerField(choices=[(1, '토요일'), (2, '일요일')])),
                ('comment', models.TextField(blank=True, default='')),
                ('accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
