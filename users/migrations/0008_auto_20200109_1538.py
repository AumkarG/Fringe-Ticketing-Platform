# Generated by Django 2.2.4 on 2020-01-09 10:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200109_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shortlisted',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, default=list, size=15),
        ),
    ]
