# Generated by Django 4.2.20 on 2025-04-19 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0008_alter_alunos_endereco_cep'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='cpf',
            field=models.CharField(default=None, help_text='Use o formato 000.000.000-00', max_length=14, validators=[django.core.validators.RegexValidator(message='CPF inválido. Use o formato 000.000.000-00', regex='^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$')], verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='alunos',
            name='email',
            field=models.EmailField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='data_de_nascimento',
            field=models.DateField(default=None, help_text='Use o formato 0000-00-00 (Ano-Mês-Dia)', validators=[django.core.validators.RegexValidator(message='Data de nascimento inválida. Use o formato 0000-00-00 (Ano-Mês-Dia)')], verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='endereco_cep',
            field=models.CharField(default=None, help_text='Use o formato 00000-000', max_length=9, validators=[django.core.validators.RegexValidator('^\\d{5}-\\d{3}$', message='Cep inválido. Use o formato 00000-000')], verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='telefone',
            field=models.CharField(default=None, help_text='Use o formato (00) 00000-0000', max_length=15, validators=[django.core.validators.RegexValidator(message='Telefone inválido. Use o formato (00) 00000-0000', regex='^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$')], verbose_name='Telefone'),
        ),
    ]
