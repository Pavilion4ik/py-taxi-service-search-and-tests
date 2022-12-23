# Generated by Django 4.1 on 2022-11-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0009_alter_car_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="comments",
            field=models.ManyToManyField(
                blank=True, related_name="comments", to="taxi.comment"
            ),
        ),
    ]
