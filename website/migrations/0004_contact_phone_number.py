# Generated by Django 4.2.5 on 2023-12-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_contact_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]