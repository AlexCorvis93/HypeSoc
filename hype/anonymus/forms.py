from django import forms
from .models import Comment




class CreateAnonymusCommentForm(forms.ModelForm):
    """COMMENT"""
    class Meta:
        model = Comment
        fields = ('text', )