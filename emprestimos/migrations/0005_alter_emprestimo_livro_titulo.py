# Generated by Django 5.0.4 on 2024-06-07 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0004_rename_livro_id_emprestimo_livro_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='livro_titulo',
            field=models.CharField(),
        ),
    ]