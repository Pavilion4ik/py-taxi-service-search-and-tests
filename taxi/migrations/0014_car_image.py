# Generated by Django 4.1 on 2022-12-19 14:30

from django.db import migrations, models
import taxi.models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0013_alter_driver_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=taxi.models.path_to_image
            ),
        ),
    ]
