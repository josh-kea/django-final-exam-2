# Generated by Django 3.1.1 on 2020-11-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telephone_number',
            field=models.IntegerField(default=12345678),
        ),
    ]
