# Generated by Django 5.1.3 on 2024-12-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_rename_name_user_nickname_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]