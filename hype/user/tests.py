from .models import Comment, Post, Profile, User
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class ProfileTest(TestCase):
    """TEST BY CREATE PROFILE"""
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test@12344', password='12test12', email='test@example.com')
        self.user.save()
        Profile.objects.create(login=self.user,
                               name='Alisa', last_name='Ivanova',
                               date_birth='2021-12-07',
                               email='test@example.com',
                               bio='Test text for biography',
                               ava=SimpleUploadedFile(name='test_image.jpg', content=open('/media/avatar/', 'rb').read(), content_type='image/jpeg'),
                               followers=Profile.followers.add(self.user)
                               )



