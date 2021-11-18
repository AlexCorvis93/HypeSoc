from django.db import models
# Create your models here.
from user.models import Post, Profile
from django.contrib.auth.models import User

class AnonymusComment(models.Model):
    """COMMENTS"""
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='')
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    text = models.TextField(max_length='200')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment on {}'.format(self.post)