from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'title', 'author', 'is_verify')
