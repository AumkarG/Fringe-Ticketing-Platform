# Generated by Django 2.2.4 on 2020-01-09 09:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191029_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shortlisted',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
