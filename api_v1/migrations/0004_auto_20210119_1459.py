# Generated by Django 3.1.5 on 2021-01-19 14:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0003_questionresponse_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresponse',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]