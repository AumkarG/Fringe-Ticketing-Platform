# Generated by Django 2.2.4 on 2020-01-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20191030_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='model_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
