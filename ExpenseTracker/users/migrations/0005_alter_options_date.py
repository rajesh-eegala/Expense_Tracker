# Generated by Django 5.0.7 on 2024-07-28 16:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_options_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]