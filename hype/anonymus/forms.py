from django import forms
from .models import AnonymusComment




class CreateAnonymusCommentForm(forms.ModelForm):
    """COMMENT"""
    class Meta:
        model = AnonymusComment
        fields = ('text', )