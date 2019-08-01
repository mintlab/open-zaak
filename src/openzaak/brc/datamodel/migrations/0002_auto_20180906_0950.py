# Generated by Django 2.0.8 on 2018-09-06 09:50

from django.db import migrations, models
import uuid
import vng_api_common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('brc_datamodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besluit',
            name='identificatie',
            field=models.CharField(default=uuid.uuid4, help_text='Identificatie van het besluit binnen de organisatie die het besluit heeft vastgesteld.', max_length=50, validators=[vng_api_common.validators.AlphanumericExcludingDiacritic()], verbose_name='identificatie'),
        ),
    ]