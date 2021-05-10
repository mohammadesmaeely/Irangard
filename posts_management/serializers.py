from rest_framework import serializers

from . import models
from user_management.serializers import UserReadSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class PostReadSerializer(serializers.ModelSerializer):
    author = UserReadSerializer()

    class Meta:
        model = models.Post
        fields = '__all__'
        depth = 1
