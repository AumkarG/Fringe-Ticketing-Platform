# Generated by Django 2.2.4 on 2020-01-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_auto_20200109_1513'),
        ('users', '0008_auto_20200109_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='shortlisted',
        ),
        migrations.AddField(
            model_name='profile',
            name='shortlisted',
            field=models.ManyToManyField(to='event.Event'),
        ),
    ]
