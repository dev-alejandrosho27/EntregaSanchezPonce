# Generated by Django 4.0.5 on 2022-08-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectgrupo', '0002_pokemons_created_pokemons_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemons',
            name='valor_unitario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
