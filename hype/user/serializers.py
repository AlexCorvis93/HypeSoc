from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from PIL import Image
from .models import Profile, Post, Category_choices, Follower

# Позже переведу все формы через апи
# Импортировал модели для сериализации-профиль,пост
class ProfileSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('login', 'name')

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowerSerializer(obj.followers.all(), many=True).data


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=1400)
    text = serializers.CharField(style={'base_template': 'textarea.html', 'rows': 7})
    category = serializers.ChoiceField(choices=Category_choices)
    img = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = Post
        fields = ('id','title', 'text', 'category', 'public_time', 'author', 'img')





class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'user')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'subscriber')