# Generated by Django 5.0.1 on 2024-01-25 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_myteams_player_myteams_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField()),
                ('team_a_goal', models.IntegerField()),
                ('team_b_goal', models.IntegerField()),
                ('team_a', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_a_matches', to='app.team')),
                ('team_b', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_b_matches', to='app.team')),
            ],
        ),
    ]