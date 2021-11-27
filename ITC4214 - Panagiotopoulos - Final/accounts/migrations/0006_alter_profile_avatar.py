# Generated by Django 3.2.8 on 2021-11-27 12:46

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='users/avatars/logo.png', upload_to=accounts.models.user_directory_path),
        ),
    ]
