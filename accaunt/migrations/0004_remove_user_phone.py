# Generated by Django 4.0.4 on 2022-05-25 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accaunt', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]