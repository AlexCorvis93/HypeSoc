from django.utils import timezone

from django.test import TestCase, Client
from .models import Post, Profile, User
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
client = Client()

def get_img():
    """FOR CREATE TEST IMG"""
    bts = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile("test.jpg", bts.getvalue())


class LikeTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='2test@12346', password='12test12', email='test@example.com')
        self.user.save()
        self.profile = Profile.objects.create(login=self.user,
                                              name='Alisa', last_name='Ivanova',
                                              date_birth='2021-12-07',
                                              email='test@example.com',
                                              bio='Test text for biography')
        self.post = Post.objects.create(title='TestPost1', text='test text test text', category='1',
                                        author=self.profile,
                                        public_time=timezone.now(),
                                        img=get_img())
        self.post.save()
        pk = self.post.pk
        response = client.get('/post/' + str(pk))