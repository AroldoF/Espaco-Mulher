# Generated by Django 5.1.5 on 2025-03-06 12:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('servicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_comprada', models.IntegerField()),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('disponivel', models.BooleanField(default=False)),
                ('data_reservada', models.DateTimeField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('disponivel', models.BooleanField(default=False)),
                ('data_reservada', models.DateTimeField()),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
