# Generated by Django 5.0.6 on 2024-06-24 03:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_post_content_alter_post_likes_feed_friendship_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='current_town',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hometown',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
