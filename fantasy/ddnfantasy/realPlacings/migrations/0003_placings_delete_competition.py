# Generated by Django 5.0.3 on 2024-03-27 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0002_initial'),
        ('realPlacings', '0002_alter_competition_actual_first_place_and_more'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_first_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_place', to='teams.team')),
                ('actual_second_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_place', to='teams.team')),
                ('actual_third_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_place', to='teams.team')),
                ('comp_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='comps.comp')),
            ],
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
    ]
