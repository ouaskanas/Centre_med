# Generated by Django 4.2.5 on 2023-09-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_rendezvous'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='num',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
