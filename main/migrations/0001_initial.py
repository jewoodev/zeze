# Generated by Django 4.1.7 on 2023-04-20 13:39

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
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("destination", models.CharField(max_length=15)),
                ("airline", models.CharField(max_length=15)),
                ("flight_number", models.CharField(max_length=15)),
            ],
        ),
    ]