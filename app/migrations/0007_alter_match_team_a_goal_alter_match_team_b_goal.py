# Generated by Django 5.0.1 on 2024-01-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_a_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_b_goal',
            field=models.IntegerField(default=0),
        ),
    ]