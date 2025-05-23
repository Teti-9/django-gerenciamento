# Generated by Django 4.2.20 on 2025-04-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0003_remove_matriculas_tempo_de_plano_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matriculas',
            old_name='tempo_restante_de_matricula',
            new_name='vencimento_da_matricula',
        ),
        migrations.RenameField(
            model_name='pagamentos',
            old_name='status_pagamento',
            new_name='status_do_pagamento',
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='tipo_de_plano',
            field=models.IntegerField(choices=[(30, 'Mensal - 30 dias.'), (90, 'Trimestral - 90 dias.'), (180, 'Semestral - 180 dias.'), (365, 'Anual - 365 dias.')], default=30, help_text='Escolha seu plano.', verbose_name='Plano'),
        ),
    ]
