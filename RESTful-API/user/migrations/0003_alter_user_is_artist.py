# Generated by Django 5.0 on 2024-02-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_blacklistedtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_artist',
            field=models.BooleanField(default=True),
        ),
    ]
