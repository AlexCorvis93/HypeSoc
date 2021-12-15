from.models import Comment, Post
from django import forms

class CreateCommentForm(forms.ModelForm):
    """COMMENT"""
    class Meta:
        model = Comment
        fields = ('name', 'text')


class PostForm(forms.ModelForm):
    """ CREATE POST"""
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))

    class Meta:
        model = Post
        fields = ('title', 'text', 'category',  'img')




















# class CreatePostForm(forms.ModelForm):
#     """POST"""
#     class Meta:
#         model = Post
#         fields = ('title', 'text', 'category', 'public_time', 'author')