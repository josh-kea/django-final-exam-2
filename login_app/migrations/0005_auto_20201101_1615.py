# Generated by Django 3.1.1 on 2020-11-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_userprofile_user_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_rank',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Silver', 'Silver'), ('Gold', 'Gold')], default='Basic', max_length=250),
        ),
    ]