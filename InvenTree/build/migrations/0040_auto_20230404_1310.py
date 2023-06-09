# Generated by Django 3.2.18 on 2023-04-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0039_auto_20230317_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='barcode_data',
            field=models.CharField(blank=True, help_text='Third party barcode data', max_length=500, verbose_name='Barcode Data'),
        ),
        migrations.AddField(
            model_name='build',
            name='barcode_hash',
            field=models.CharField(blank=True, help_text='Unique hash of barcode data', max_length=128, verbose_name='Barcode Hash'),
        ),
    ]
