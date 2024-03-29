# Generated by Django 4.2.5 on 2023-10-01 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_remove_rendezvous_medecin_rendezvous_medecin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='medecin',
            field=models.ManyToManyField(to='pages.medecin'),
        ),
        migrations.CreateModel(
            name='FicheP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('tel', models.CharField(max_length=15)),
                ('date', models.DateTimeField()),
                ('desc', models.TextField()),
                ('per', models.OneToOneField(limit_choices_to={'groups__isnull': True}, on_delete=django.db.models.deletion.CASCADE, to='pages.patient')),
            ],
        ),
    ]
