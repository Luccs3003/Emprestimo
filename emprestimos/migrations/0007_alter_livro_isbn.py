# Generated by Django 5.0.4 on 2024-06-07 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0006_alter_emprestimo_livro_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]
