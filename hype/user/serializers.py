from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from PIL import Image
from .models import Profile, Post, Category_choices


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('login', 'name')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=400,  style={'placeholder': 'Title', 'autofocus': True, 'input_type': 'title'})
    text = serializers.CharField(max_length=1000, style={'base_template': 'textarea.html', 'rows': 4, 'placeholder': 'Text'})
    category = serializers.ChoiceField(choices=Category_choices, style={'base_template': 'select.html'})
    img = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'category', 'public_time', 'author', 'img']






