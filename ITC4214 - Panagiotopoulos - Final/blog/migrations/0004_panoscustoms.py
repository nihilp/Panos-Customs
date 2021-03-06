# Generated by Django 3.2.8 on 2021-11-26 14:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200815_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='PanosCustoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=30, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
    ]
