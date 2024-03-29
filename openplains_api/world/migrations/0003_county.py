# Generated by Django 4.1.2 on 2022-10-17 19:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_huc12'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('statefp', models.CharField(max_length=2, verbose_name='statefp')),
                ('countyfp', models.CharField(max_length=3, verbose_name='countyfp')),
                ('countyns', models.CharField(max_length=8, verbose_name='countyns')),
                ('affgeoid', models.CharField(max_length=14, verbose_name='affgeoid')),
                ('geoid', models.CharField(max_length=5, verbose_name='geoid')),
                ('lsad', models.IntegerField(max_length=2, verbose_name='lsad')),
                ('aland', models.BigIntegerField()),
                ('awater', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
