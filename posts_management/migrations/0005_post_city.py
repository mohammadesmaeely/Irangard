# Generated by Django 2.2 on 2021-02-02 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0002_city_state'),
        ('posts_management', '0004_auto_20210201_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='system_management.City', verbose_name='شهر'),
        ),
    ]
