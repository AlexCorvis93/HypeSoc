from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    login = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=90,  default='')
    last_name = models.CharField(max_length=90,  default='')
    date_birth = models.DateField(max_length=9)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    bio = models.TextField(max_length=140)
    ava = models.ImageField(upload_to='avatar/', blank=True, null=True, default="add photo")
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    @property
    def is_authenticated(self):
        """examination if user is authentificated"""
        return True

    def __str__(self):
        return self.name


Category_choices = [
        (1, 'Art'),
        (2, 'business'),
        (3, 'science ')
    ]


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(verbose_name='text')
    category = models.PositiveSmallIntegerField('category', choices=Category_choices)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    public_time = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='posts/', blank=True, null=True, default="add img")
    likes = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(max_length='300')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


