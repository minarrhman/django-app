# Generated by Django 3.1.3 on 2020-11-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
