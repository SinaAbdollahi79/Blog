# Generated by Django 4.2.5 on 2023-11-15 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_alter_contact_options_contact_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="last_name",
            field=models.CharField(default="", max_length=50),
        ),
    ]
