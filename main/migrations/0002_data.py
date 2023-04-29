# Generated by Django 4.1.7 on 2023-04-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specific_id",
                    models.CharField(max_length=156, verbose_name="specific_id"),
                ),
                (
                    "horizon_width",
                    models.CharField(max_length=100, verbose_name="horizon_width"),
                ),
                (
                    "vertical_width",
                    models.CharField(max_length=100, verbose_name="vertical_width"),
                ),
                (
                    "x_location",
                    models.CharField(max_length=100, verbose_name="x_location"),
                ),
                (
                    "y_location",
                    models.CharField(max_length=100, verbose_name="y_location"),
                ),
            ],
        ),
    ]
