# Generated by Django 4.1 on 2023-02-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orders",
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
                ("title", models.CharField(default="", max_length=70)),
                ("paper_length", models.CharField(default="", max_length=70)),
                ("topic", models.CharField(default="", max_length=70)),
                ("audience", models.CharField(default="", max_length=70)),
                ("written_in", models.CharField(default="", max_length=70)),
                ("email", models.CharField(default="", max_length=70)),
                ("deadline", models.CharField(default="", max_length=200)),
                ("paid", models.BooleanField(default=False)),
            ],
        ),
    ]