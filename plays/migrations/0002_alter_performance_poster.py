# Generated by Django 4.2.13 on 2024-05-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plays", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="performance",
            name="poster",
            field=models.FileField(upload_to="posters/"),
        ),
    ]
