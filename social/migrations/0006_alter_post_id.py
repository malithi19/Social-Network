# Generated by Django 5.0.6 on 2024-06-24 17:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_remove_userprofile_current_town_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]