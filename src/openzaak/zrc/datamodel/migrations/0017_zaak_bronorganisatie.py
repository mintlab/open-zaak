# Generated by Django 2.0.6 on 2018-07-16 12:42

from django.db import migrations
import vng_api_common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0016_auto_20180711_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaak',
            name='bronorganisatie',
            field=vng_api_common.fields.RSINField(default='', help_text='Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die de zaak heeft gecreeerd.', max_length=9),
            preserve_default=False,
        ),
    ]