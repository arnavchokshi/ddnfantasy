# Generated by Django 5.0.3 on 2024-03-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='top_teams',
            field=models.JSONField(default={}),
        ),
    ]
