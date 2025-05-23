# Generated by Django 4.2.20 on 2025-04-23 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0013_cancelarmatricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancelarmatricula',
            old_name='cancelamentos',
            new_name='cancelamento',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='plano',
        ),
        migrations.AddField(
            model_name='matricula',
            name='assinatura',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='assinatura_efi_id'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='pagamento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento', to='matriculas.matricula'),
        ),
        migrations.DeleteModel(
            name='GerarPagamento',
        ),
    ]
