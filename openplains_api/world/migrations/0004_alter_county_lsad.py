# Generated by Django 4.1.2 on 2022-10-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='lsad',
            field=models.CharField(max_length=2, verbose_name='lsad'),
        ),
    ]
