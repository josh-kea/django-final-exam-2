# Generated by Django 3.1.3 on 2021-02-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0002_auto_20210208_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_status',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isEmployee',
            field=models.BooleanField(default=False),
        ),
    ]
