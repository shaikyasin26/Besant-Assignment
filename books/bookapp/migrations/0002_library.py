# Generated by Django 5.0 on 2023-12-05 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Library",
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
                ("name", models.CharField(max_length=100)),
                ("membership_details", models.CharField(max_length=200)),
                (
                    "ISBM",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bookapp.book"
                    ),
                ),
            ],
        ),
    ]
