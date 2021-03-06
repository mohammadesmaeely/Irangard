# Generated by Django 2.2 on 2021-02-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='شناسه')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('message', models.TextField(verbose_name='پیام')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='تاریخ ساخت')),
            ],
            options={
                'verbose_name': 'تیکت',
                'verbose_name_plural': 'تیکت ها',
            },
        ),
    ]
