from.models import Post, Comment
from django import forms


class CreateCommentForm(forms.ModelForm):
    """COMMENT"""
    class Meta:
        model =Comment
        fields = ('name', 'body')























# class CreatePostForm(forms.ModelForm):
#     """POST"""
#     class Meta:
#         model = Post
#         fields = ('title', 'text', 'category', 'public_time', 'author')