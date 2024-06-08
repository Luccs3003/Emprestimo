# Generated by Django 5.0.4 on 2024-06-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro_id', models.IntegerField()),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('emprestado_para', models.CharField(max_length=100)),
            ],
        ),
    ]