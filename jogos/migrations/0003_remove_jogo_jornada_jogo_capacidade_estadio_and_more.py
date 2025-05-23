# Generated by Django 5.2.1 on 2025-05-16 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0002_liga_jornada_liga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogo',
            name='jornada',
        ),
        migrations.AddField(
            model_name='jogo',
            name='capacidade_estadio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogo',
            name='liga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jogos.liga'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='odd_casa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='jogo',
            name='odd_empate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='jogo',
            name='odd_fora',
            field=models.FloatField(default=0.0),
        ),
        migrations.DeleteModel(
            name='Jornada',
        ),
    ]
