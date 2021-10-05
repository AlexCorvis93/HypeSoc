from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    """show user profile"""
    login = models.OneToOneField(User.USERNAME_FIELD, on_delete=models.CASCADE)
    name = models.OneToOneField(User.first_name, on_delete=models.CASCADE)
    date_birth = models.DateField(max_length=8)
    bio = models.TextField(max_length=140)
    ava = models.ImageField(upload_to='media/avatar/', blank=True, null=True)

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
    autor = models.OneToOneField(Profile, default=0, on_delete=models.CASCADE)
    public_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


