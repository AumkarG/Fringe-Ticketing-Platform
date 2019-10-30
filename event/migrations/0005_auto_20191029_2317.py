# Generated by Django 2.2.4 on 2019-10-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='model_pic',
            field=models.ImageField(default='C:/Users/aumkar/Pictures/Screenshots', upload_to='Djangoimages/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(choices=[('South Bombay', 'South Bombay'), ('Western Suburbs', 'Western Suburbs'), ('Eastern Suburbs', 'Eastern Suburbs'), ('North Mumbai', 'North Mumbai')], default='South Bombay', max_length=50),
        ),
    ]