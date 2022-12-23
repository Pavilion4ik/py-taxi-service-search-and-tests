# Generated by Django 4.1 on 2022-11-12 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0010_alter_car_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="comments",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="comments", to="taxi.comment"
            ),
        ),
    ]
