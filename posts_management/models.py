from django.db import models
from user_management.models import User
from system_management.models import SoftDeleteManager, City


class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='شناسه')
    name = models.CharField(max_length=200, verbose_name='نام')

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوع ها'

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='شناسه')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    description = models.TextField(verbose_name='شرح')
    image = models.ImageField(upload_to='images/posts_image', verbose_name='عکس پست')
    image2 = models.ImageField(null=True, blank=True, default=None, upload_to='images/posts_image', verbose_name='عکس پست')
    image3 = models.ImageField(null=True, blank=True, default=None, upload_to='images/posts_image', verbose_name='عکس پست')
    is_verify = models.BooleanField(default=True, verbose_name='تایید شده؟')
    visit = models.BigIntegerField(default=0, verbose_name='تعداد بازدید')
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.PROTECT, default=None, verbose_name='شهر')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت پست')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین به روز رسانی پست')
    deleted_at = models.DateTimeField(null=True, blank=True, default=None, verbose_name='تاریخ حذف شدن پست')

    objects = SoftDeleteManager()

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

