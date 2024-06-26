# Generated by Django 4.2.5 on 2024-01-22 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.post",
            ),
            preserve_default=False,
        ),
    ]
