# Generated by Django 4.1.6 on 2023-11-06 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='closeTime',
            field=models.TimeField(default=datetime.time(0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='openTime',
            field=models.TimeField(default=datetime.time(0, 0)),
            preserve_default=False,
        ),
    ]