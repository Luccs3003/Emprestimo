# Generated by Django 5.0.4 on 2024-06-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0008_alter_livro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(),
        ),
    ]
