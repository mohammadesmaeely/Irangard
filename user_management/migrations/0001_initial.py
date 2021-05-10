# Generated by Django 3.1.4 on 2020-12-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='شناسه')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='نام کاربری')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='نام خانوادگی')),
                ('phone_number', models.CharField(blank=True, max_length=13, verbose_name='شماره تلفن')),
                ('national_code', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('address', models.TextField(blank=True, verbose_name='آدرس')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_management/images/user_image', verbose_name='عکس کاربر')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت کاربران')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین به روز رسانی کاربر')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='تاریخ حذف شدن کاربر')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
