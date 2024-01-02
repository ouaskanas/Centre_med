# Generated by Django 4.2.5 on 2023-10-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_remove_rendezvous_medecin_rendezvous_medecin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendezvous',
            name='medecin',
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='medecin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.medecin'),
        ),
    ]
