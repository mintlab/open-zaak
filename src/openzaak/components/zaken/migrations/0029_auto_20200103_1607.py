# Generated by Django 2.2.9 on 2020-01-03 16:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zaken", "0028_auto_20191220_1439"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zaakobject",
            name="object_type_overige",
            field=models.CharField(
                blank=True,
                help_text='Beschrijft het type OBJECT als `objectType` de waarde "overige" heeft.',
                max_length=100,
                validators=[django.core.validators.RegexValidator("[a-z_]+")],
            ),
        ),
    ]