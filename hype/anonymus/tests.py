from django.shortcuts import get_object_or_404
from io import BytesIO
from django.urls import reverse
from django.utils import timezone
from .models import Comment, Post, Profile, User
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

client = Client()
def get_img():
    """FOR CREATE TEST IMG"""
    bts = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile("test.jpg", bts.getvalue())

class ListTest(TestCase):
    """MAIN PAGE TEST"""

    def test_list_post(self):
        response = client.get(reverse('a_news'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'anonymus/anonym_news.html')








class CommentViewTest(TestCase):
    def setUp(self) -> None:
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



    def test_comment_view(self):
        pk = self.post.pk
        self.detail = client.get('/post/' + str(pk))
        self.assertEqual(self.detail.status_code, 200)
        client.post(self.detail, {'text': 'comment text'})
        self.assertEqual(Comment.objects.first().text, 'comment text')
