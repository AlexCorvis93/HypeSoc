from django.utils import timezone
from django.urls import reverse
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
        self.another_user= User.objects.create(username='3test@12', password='12test12', email='test@example.com')
        self.post = Post.objects.create(title='TestPost1', text='test text test text', category='1',
                                        author=self.profile,
                                        public_time=timezone.now(),
                                        img=get_img())
        self.post.save()

    def test_like_get(self):
        """add 1 Like and remove"""
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        pk = self.post.pk
        response = client.get('/post/' + str(pk))
        self.assertEqual(response.status_code, 200)
        self.post.likes.add(self.another_user)
        like_api = reverse('like', args=[str(pk)])
        response_like_add = client.get(like_api)
        self.assertEqual(response_like_add.status_code, 200)
        self.assertEqual(response_like_add.data['liked'], True)
        self.assertEqual(response_like_add.data['updated'], True)
        self.post.likes.remove(self.another_user)
        response_like_del = client.get(like_api)
        self.assertEqual(response_like_del.status_code, 200)
        self.assertEqual(response_like_del.data['liked'], False)
        self.assertEqual(response_like_del.data['updated'], False)

