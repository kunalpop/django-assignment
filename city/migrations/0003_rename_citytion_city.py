# Generated by Django 5.1.5 on 2025-02-07 08:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("city", "0002_rename_location_citytion"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Citytion",
            new_name="City",
        ),
    ]
