# Generated by Django 2.2.4 on 2019-10-29 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20191028_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
