from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from PIL import Image
from .models import Post, Category_choices



class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=400,  style={'placeholder': "title"})
    category = serializers.ChoiceField(choices=Category_choices)
    img = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'category', 'public_time', 'author', 'img']






