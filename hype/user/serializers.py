from rest_framework import serializers

from .models import Profile, Post


# Импортировал модели для сериализации-профиль,пост
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('login', 'name', 'bio', 'ava')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'public_time', 'autor')
