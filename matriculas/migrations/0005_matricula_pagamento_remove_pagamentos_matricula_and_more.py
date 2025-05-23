# Generated by Django 4.2.20 on 2025-04-19 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0009_alunos_cpf_alunos_email_and_more'),
        ('matriculas', '0004_rename_tempo_restante_de_matricula_matriculas_vencimento_da_matricula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.IntegerField(choices=[(30, 'Mensal - 30 dias (R$ 40,00)'), (90, 'Trimestral - 90 dias (R$ 60,00)'), (180, 'Semestral - 180 dias (R$ 99,00)'), (365, 'Anual - 365 dias (R$ 120,00)')], default=30, help_text='Escolha seu plano.', verbose_name='preço')),
                ('plano', models.TextField(blank=True, default=None, null=True, verbose_name='plano_efi_id')),
                ('data_da_matricula', models.DateTimeField(auto_now_add=True)),
                ('vencimento_da_matricula', models.DateField(blank=True, null=True)),
                ('status_da_matricula', models.CharField(blank=True, default='inativo', max_length=255, null=True, verbose_name='status da matrícula')),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='matricula', to='alunos.alunos')),
            ],
            options={
                'verbose_name_plural': 'Matrículas',
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinatura', models.TextField(blank=True, default=None, null=True, verbose_name='assinatura_efi_id')),
                ('status_do_pagamento', models.CharField(blank=True, default='pendente', max_length=255, null=True, verbose_name='status do pagamento')),
                ('matricula', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento', to='matriculas.matricula')),
            ],
            options={
                'verbose_name_plural': 'Pagamento',
            },
        ),
        migrations.RemoveField(
            model_name='pagamentos',
            name='matricula',
        ),
        migrations.DeleteModel(
            name='Matriculas',
        ),
        migrations.DeleteModel(
            name='Pagamentos',
        ),
    ]
