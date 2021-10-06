from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    """show user profile"""
    class Meta:
        db_table = "профиль"

    login = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user_login', default=None)
    name = models.CharField(max_length=111, default='')
    date_birth = models.DateField(max_length=9)
    bio = models.TextField(max_length=140)
    ava = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """custom post"""
    class Meta:
        db_table = "пост"

    Category_choices = [
        (1, 'Art'),
        (2, 'business'),
        (3, 'science ')
    ]
    title = models.CharField(max_length=140)
    text = models.TextField(verbose_name='text')
    category = models.PositiveSmallIntegerField('category', choices=Category_choices)
    autor = models.ForeignKey(Profile, default='', on_delete=models.CASCADE)
    public_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


