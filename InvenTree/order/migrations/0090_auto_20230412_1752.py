# Generated by Django 3.2.18 on 2023-04-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0089_auto_20230404_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='description',
            field=models.CharField(blank=True, help_text='Order description (optional)', max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='returnorder',
            name='description',
            field=models.CharField(blank=True, help_text='Order description (optional)', max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='description',
            field=models.CharField(blank=True, help_text='Order description (optional)', max_length=250, verbose_name='Description'),
        ),
    ]
