# Generated by Django 4.2.13 on 2024-05-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0002_play_date_play_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='poster',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
