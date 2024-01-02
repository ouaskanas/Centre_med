# Generated by Django 4.2.5 on 2023-09-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_delete_medimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=10)),
                ('specialite', models.CharField(max_length=15)),
            ],
        ),
    ]