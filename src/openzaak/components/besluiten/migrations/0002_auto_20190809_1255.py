# Generated by Django 2.2.2 on 2019-08-09 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('besluiten', '0001_initial'),
        ('catalogi', '0001_initial'),
        ('documenten', '0001_initial'),
        ('zaken', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='besluit',
            name='_zaakbesluit',
        ),
        migrations.AlterField(
            model_name='besluit',
            name='besluittype',
            field=models.ForeignKey(help_text='Referentie naar het BESLUITTYPE (in de Catalogi API).', on_delete=django.db.models.deletion.CASCADE, to='catalogi.BesluitType'),
        ),
        migrations.AlterField(
            model_name='besluit',
            name='zaak',
            field=models.ForeignKey(blank=True, help_text='Referentie naar de ZAAK (in de Zaken API) waarvan dit besluit uitkomst is.', null=True, on_delete=django.db.models.deletion.PROTECT, to='zaken.Zaak'),
        ),
        migrations.AlterField(
            model_name='besluitinformatieobject',
            name='informatieobject',
            field=models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT (in de Documenten API) waarin (een deel van) het besluit beschreven is.', on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical'),
        ),
    ]