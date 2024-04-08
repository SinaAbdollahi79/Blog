# Generated by Django 4.2.5 on 2024-01-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_categories_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="comment",
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
                ("email", models.EmailField(max_length=254)),
                ("subject", models.TextField(max_length=100)),
                ("message", models.TextField(max_length=250)),
                ("approved", models.BooleanField(default=False)),
                ("create_date", models.DateField(auto_now_add=True)),
                ("updated_date", models.DateField(auto_now=True)),
            ],
        ),
    ]
