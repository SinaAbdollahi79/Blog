# Generated by Django 4.2.5 on 2024-04-08 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_remove_post_published_post_published_first_page"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="published_first_page",
            new_name="first_page_published",
        ),
    ]