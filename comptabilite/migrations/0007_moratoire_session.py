# Generated by Django 4.2 on 2023-06-18 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_etudiant_classe'),
        ('comptabilite', '0006_moratoire_tranche'),
    ]

    operations = [
        migrations.AddField(
            model_name='moratoire',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.session'),
            preserve_default=False,
        ),
    ]
