# Generated by Django 5.0 on 2023-12-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0005_borrow_borrowing_dt_borrow_return_dt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrow",
            name="return_dt",
            field=models.DateTimeField(),
        ),
    ]
