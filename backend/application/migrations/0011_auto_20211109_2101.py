# Generated by Django 3.2.9 on 2021-11-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_alter_climatedata_time'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='climatedata',
            name='humidity_range',
        ),
        migrations.RemoveIndex(
            model_name='climatedata',
            name='time_idx',
        ),
        migrations.AlterField(
            model_name='climatedata',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddConstraint(
            model_name='climatedata',
            constraint=models.CheckConstraint(check=models.Q(('humidity__gte', 0.0), ('humidity__lte', 100.0)), name='climatedata_humidity_range'),
        ),
    ]
