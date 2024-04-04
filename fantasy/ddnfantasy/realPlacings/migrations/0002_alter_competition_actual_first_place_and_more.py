# Generated by Django 5.0.3 on 2024-03-27 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realPlacings', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='actual_first_place',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actual_first_place', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='actual_second_place',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actual_second_place', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='actual_third_place',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actual_third_place', to='teams.team'),
        ),
    ]
