# Generated by Django 2.2.13 on 2020-08-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200819_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_purchase_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
