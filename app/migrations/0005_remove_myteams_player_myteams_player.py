# Generated by Django 5.0.1 on 2024-01-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_myteams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myteams',
            name='player',
        ),
        migrations.AddField(
            model_name='myteams',
            name='player',
            field=models.ManyToManyField(to='app.player'),
        ),
    ]