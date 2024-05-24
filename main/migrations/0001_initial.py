# Generated by Django 5.0.6 on 2024-05-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("task", models.CharField(max_length=255)),
                ("is_completed", models.BooleanField(default=False)),
                ("created_date", models.DateField(auto_now=True)),
                ("updated_date", models.DateField(auto_now=True)),
            ],
        ),
    ]
