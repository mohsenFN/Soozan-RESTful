# Generated by Django 5.0 on 2024-01-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_artist',
            field=models.BooleanField(),
        ),
    ]
