# Generated by Django 4.2.5 on 2023-10-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="post",
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
                ("titel", models.CharField(max_length=100)),
                ("content", models.TextField()),
            ],
        ),
    ]
