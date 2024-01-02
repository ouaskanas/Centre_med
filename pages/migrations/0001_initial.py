# Generated by Django 4.2.5 on 2023-09-27 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=3)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('libre', models.BooleanField(default=True)),
            ],
        ),
    ]