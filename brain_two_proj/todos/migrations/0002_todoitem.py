# Generated by Django 4.2.4 on 2023-08-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TodoItem",
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
                ("task", models.CharField(max_length=100)),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                ("is_completed", models.BooleanField(default=False)),
            ],
        ),
    ]