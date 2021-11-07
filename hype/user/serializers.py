from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Profile, Post

# Позже переведу все формы через апи
# Импортировал модели для сериализации-профиль,пост
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('login', 'name', 'bio', 'ava')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'category', 'public_time', 'author')


class PostSerializerCreate(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id','title', 'text', 'category', 'public_time', 'author')

        def create(self, validated_data):
            return Post.objects.all()(**validated_data)

        def update(self, instance, validated_data):

            instance.title = validated_data.get('title', instance.title)
            instance.text = validated_data.get('text', instance.text)
            instance.category = validated_data.get('category', instance.category)
            instance.author = validated_data.get('author', instance.author)
            instance.save()
            return instance







