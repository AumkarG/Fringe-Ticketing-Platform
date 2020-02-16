# Generated by Django 2.2.4 on 2020-01-09 09:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_shortlisted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shortlisted',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=1, size=15),
            preserve_default=False,
        ),
    ]