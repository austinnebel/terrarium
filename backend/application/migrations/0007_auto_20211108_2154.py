# Generated by Django 3.2.9 on 2021-11-09 03:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20211104_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=12)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='climatedata',
            name='humidity',
            field=models.FloatField(max_length=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='climatedata',
            name='temperature',
            field=models.FloatField(max_length=6),
        ),
    ]
