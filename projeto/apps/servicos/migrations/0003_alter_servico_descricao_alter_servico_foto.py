# Generated by Django 5.1.5 on 2025-02-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
