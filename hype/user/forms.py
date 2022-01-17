from.models import Comment, Post
from django import forms

Category_choices = [
        (1, 'Art'),
        (2, 'business'),
        (3, 'science ')
    ]

class CreateCommentForm(forms.ModelForm):
    """COMMENT"""
    text = forms.CharField(label='Your text:')
    class Meta:
        model = Comment
        fields = ('name', 'text')


class PostForm(forms.ModelForm):
    """ CREATE POST"""
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Text', 'rows': 4}))
    category = forms.ChoiceField(label='', choices=Category_choices)
    class Meta:
        model = Post
        fields = ('title', 'text', 'category',  'img')




















# class CreatePostForm(forms.ModelForm):
#     """POST"""
#     class Meta:
#         model = Post
#         fields = ('title', 'text', 'category', 'public_time', 'author')