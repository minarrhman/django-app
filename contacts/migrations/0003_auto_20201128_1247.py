# Generated by Django 3.1.3 on 2020-11-28 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20201128_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 11, 28, 12, 47, 24, 548384, tzinfo=utc)),
        ),
    ]