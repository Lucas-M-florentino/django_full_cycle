# Generated by Django 5.0.1 on 2024-01-25 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_match_team_a_goal_alter_match_team_b_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_a_matches', to='app.team', verbose_name='Time A'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_b_matches', to='app.team', verbose_name='Time B'),
        ),
        migrations.AlterField(
            model_name='myteams',
            name='player',
            field=models.ManyToManyField(to='app.player', verbose_name='Jogador'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
    ]