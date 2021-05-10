from django.db import models


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__exact=None)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='شناسه')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    message = models.TextField(verbose_name='پیام')

    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.title


class State(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='شناسه')
    name = models.CharField(max_length=200, verbose_name='نام استان')

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='شناسه')
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='استان')
    name = models.CharField(max_length=200, verbose_name='شهر')

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'

    def __str__(self):
        return self.name
