# Generated by Django 2.2.2 on 2019-07-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0079_auto_20190717_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rol',
            old_name='rolomschrijving',
            new_name='omschrijving_generiek',
        ),
    ]