# Generated by Django 4.2 on 2023-06-17 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_etudiant_classe'),
        ('comptabilite', '0005_rename_name_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moratoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Motif', models.TextField()),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Elève', to='main.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Tranche',
            fields=[
                ('echeancepaiement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comptabilite.echeancepaiement')),
                ('moratoire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comptabilite.moratoire')),
            ],
            bases=('comptabilite.echeancepaiement',),
        ),
    ]