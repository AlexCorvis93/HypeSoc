from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Profile, Post, Category_choices

# Позже переведу все формы через апи
# Импортировал модели для сериализации-профиль,пост
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('login', 'name', 'bio', 'ava')


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=1400, style={'base_template': 'textarea.html', 'rows': 2})
    text = serializers.CharField(style={'base_template': 'textarea.html', 'rows': 4})
    category = serializers.ChoiceField(choices=Category_choices, style={'base_template': 'select.html'})

    class Meta:
        model = Post
        fields = ('id','title', 'text', 'category', 'public_time', 'author')









