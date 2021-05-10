from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    model = models.User
    list_display = ('id', 'username')

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = models.User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()
