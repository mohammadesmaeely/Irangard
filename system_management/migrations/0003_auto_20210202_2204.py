# Generated by Django 2.2 on 2021-02-02 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0002_city_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'شهر', 'verbose_name_plural': 'شهرها'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'استان', 'verbose_name_plural': 'استان ها'},
        ),
    ]
