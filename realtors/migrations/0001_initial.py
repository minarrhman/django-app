# Generated by Django 3.1.3 on 2020-11-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='realtors')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('descrption', models.TextField(blank=True)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateField(blank=True)),
            ],
        ),
    ]
