from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, national_code):
        user = self.model(username=username, national_code=national_code)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, national_code):
        user = self.create_user(username=username, password=password, national_code=national_code)
        user.is_admin = True
        user.save(using=self._db)
        return user

    # def get_queryset(self):
    #     return super().get_queryset().filter(deleted_at__exact=None)


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, verbose_name='شناسه')
    username = models.CharField(unique=True, max_length=100, verbose_name='نام کاربری')
    first_name = models.CharField(max_length=100, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='نام خانوادگی')
    phone_number = models.CharField(blank=True, max_length=13, verbose_name='شماره تلفن')
    national_code = models.CharField(blank=True, null=True, default=True, max_length=10, verbose_name='کد ملی')
    # password = models.TextField(verbose_name='رمز عبور')
    address = models.TextField(blank=True, verbose_name='آدرس')
    image = models.ImageField(upload_to='user_management/images/user_image', null=True, blank=True, default=None,
                              verbose_name='عکس کاربر')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت کاربران')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین به روز رسانی کاربر')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['national_code']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.first_name + " \t " + self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

