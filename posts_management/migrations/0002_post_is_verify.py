# Generated by Django 3.1.4 on 2021-01-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_verify',
            field=models.BooleanField(default=False, verbose_name='تایید شده؟'),
        ),
    ]
