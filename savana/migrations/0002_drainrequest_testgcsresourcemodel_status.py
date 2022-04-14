# Generated by Django 4.0.4 on 2022-04-13 22:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrainRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('coordinate', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='testgcsresourcemodel',
            name='status',
            field=models.CharField(choices=[('AC', 'accepted'), ('RN', 'running'), ('FN', 'finished'), ('TM', 'terminated'), ('ER', 'error')], default='AC', max_length=2),
        ),
    ]
