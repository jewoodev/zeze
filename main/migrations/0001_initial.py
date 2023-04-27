# Generated by Django 4.1.7 on 2023-04-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
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
                ("departure_time", models.TimeField()),
                ("destination", models.CharField(max_length=30)),
                ("airline", models.CharField(max_length=15)),
                ("flight_number", models.CharField(max_length=15)),
                ("terminal", models.CharField(max_length=5)),
                ("gate", models.CharField(max_length=10)),
                ("date", models.DateField()),
            ],
        ),
    ]
