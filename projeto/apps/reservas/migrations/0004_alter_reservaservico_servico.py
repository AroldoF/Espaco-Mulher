# Generated by Django 5.1.5 on 2025-02-24 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_remove_reservaservico_tempo_duracao'),
        ('servicos', '0005_alter_servico_tempo_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaservico',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servico'),
        ),
    ]
