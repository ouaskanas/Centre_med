# Generated by Django 4.2.5 on 2023-09-27 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_medecin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medecin',
            name='image',
        ),
    ]