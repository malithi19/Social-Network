# Generated by Django 5.0.6 on 2024-06-24 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_alter_userprofile_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='current_town',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hometown',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='work',
        ),
    ]
