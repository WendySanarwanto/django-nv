# Generated by Django 3.2.18 on 2023-03-04 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 14, 56, 32, 209152, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 14, 56, 32, 209980, tzinfo=utc), verbose_name='date due'),
        ),
    ]
