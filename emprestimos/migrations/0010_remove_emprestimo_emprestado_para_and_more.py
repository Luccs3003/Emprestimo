# Generated by Django 5.0.4 on 2024-06-09 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0009_alter_livro_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='emprestado_para',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='livro_titulo',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emprestimos.livro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emprestimos.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
