# Generated by Django 3.1.4 on 2021-01-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.CharField(blank=True, default=True, max_length=10, null=True, verbose_name='کد ملی'),
        ),
    ]
