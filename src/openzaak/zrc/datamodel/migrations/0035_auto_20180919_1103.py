# Generated by Django 2.0.6 on 2018-09-19 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0034_auto_20180817_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZaakInformatieObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informatieobject', models.URLField(help_text='URL-referentie naar het informatieobject in het DRC, waar ook de relatieinformatie opgevraagd kan worden.', verbose_name='informatieobject')),
                ('zaak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zrc_datamodel.Zaak')),
            ],
            options={
                'verbose_name': 'zaakinformatieobject',
                'verbose_name_plural': 'zaakinformatieobjecten',
            },
        ),
        migrations.AlterField(
            model_name='zaakobject',
            name='object_type',
            field=models.CharField(choices=[('VerblijfsObject', 'Verblijfsobject'), ('MeldingOpenbareRuimte', 'Melding openbare ruimte'), ('InzageVerzoek', 'Inzage verzoek in het kader van de AVG')], help_text='Beschrijft het type object gerelateerd aan de zaak', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='zaakinformatieobject',
            unique_together={('zaak', 'informatieobject')},
        ),
    ]