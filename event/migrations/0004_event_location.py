# Generated by Django 2.2.4 on 2019-10-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20191029_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default='Mumbai'),
        ),
    ]
