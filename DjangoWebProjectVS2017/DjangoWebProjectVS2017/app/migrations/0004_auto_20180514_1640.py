# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-14 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_quizchoice_quizquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizchoice',
            name='correctAnswer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quizchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.QuizQuestion'),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='topic',
            field=models.CharField(choices=[('Trabajo final HADS', 'Trabajo final HADS'), ('Evaluación HADS', 'Evaluación HADS'), ('Informática', 'Informática'), ('Otro', 'Otro')], default='TFHADS', max_length=6),
        ),
    ]