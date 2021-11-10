from django.db import models
from django.utils import timezone
from PIL import Image

from django.contrib.auth.models import User

Category_choices = [
        (1, 'Art'),
        (2, 'business'),
        (3, 'science ')
    ]

class Profile(models.Model):
    """show and create user profile"""
    class Meta:
        db_table = "профиль"

    login = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='login_user', default='')
    name = models.CharField(max_length=90,  default='')
    last_name = models.CharField(max_length=90,  default='')
    date_birth = models.DateField(max_length=9)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    bio = models.TextField(max_length=140)
    ava = models.ImageField(upload_to='avatar/', blank=True, null=True, default="add photo")

    @property
    def is_authenticated(self):
        """examination if user is authentificated"""
        return True

    def __str__(self):
        return self.name


class Post(models.Model):
    """custom post"""
    Category_choices = [
        (1, 'Art'),
        (2, 'business'),
        (3, 'science ')
    ]

    title = models.CharField(max_length=140)
    text = models.TextField(verbose_name='text')
    category = models.PositiveSmallIntegerField('category', choices=Category_choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    public_time = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='posts/', blank=True, null=True, default="add img")

    @property
    def is_authenticated(self):
        """examination if user is authentificated"""
        return True

    def in_img(self):
        if self.img:
            return u'<img src="%s" width="350" height="350" />' % self.img.url
        else:
            return '(Sin imagen)'

    def __str__(self):
        return self.title



class Follower(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f'{self.subscriber} is followed by {self.user}'


class Comment(models.Model):
    """COMMENTS"""
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length='200')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)