# Generated by Django 3.1.5 on 2021-01-18 17:28

import api_v1.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', api_v1.models.UserManager()),
            ],
        ),
    ]