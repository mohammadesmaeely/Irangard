# Generated by Django 3.1.4 on 2021-01-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_remove_user_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user_management/images/user_image', verbose_name='عکس کاربر'),
        ),
    ]
