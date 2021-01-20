# Generated by Django 3.1.5 on 2021-01-19 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0004_auto_20210119_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='mentor',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Mentors'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]