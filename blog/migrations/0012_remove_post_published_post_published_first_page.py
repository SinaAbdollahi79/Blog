# Generated by Django 4.2.5 on 2024-04-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_post_page_titel_post_published"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="published",
        ),
        migrations.AddField(
            model_name="post",
            name="published_first_page",
            field=models.BooleanField(default=False),
        ),
    ]
