# Generated by Django 4.0.2 on 2022-02-18 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_create_team_team_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='project',
            name='department',
        ),
    ]
