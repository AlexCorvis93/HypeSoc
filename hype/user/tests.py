from django.shortcuts import get_object_or_404, redirect
from io import BytesIO
import json
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


class ProfileTest(TestCase):
    """TEST BY CREATE PROFILE """
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test@12344', password='12test12', email='test@example.com')
        self.user.save()

        self.profile = Profile.objects.create(login=self.user,
                               name='Alisa', last_name='Ivanova',
                               date_birth='2021-12-07',
                               email='test@example.com',
                               bio='Test text for biography',
                               ava=get_img())

        self.pk = self.profile.pk
        self.user_page_url = reverse('profile_page', args=[str(self.pk)])

    def test_url_profile(self):
        client.post('/accounts/login/', {'username': 'test@12344', 'password': '12test12'}, follow=True)
        response = client.get('/api/personal_page/')
        self.assertEqual(response.status_code, 200)

    def test_another_profile(self):
        client.post('/accounts/login/', {'username': 'test@12344', 'password': '12test12'}, follow=True)
        response = client.get(self.user_page_url)
        self.assertEqual(response.status_code, 200)


class PostTest(TestCase):
    """Create post in DATABASE test"""
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='2test@12346', password='12test12', email='test@example.com')
        self.user.save()
        self.profile = Profile.objects.create(login=self.user,
                               name='Alisa', last_name='Ivanova',
                               date_birth='2021-12-07',
                               email='test@example.com',
                               bio='Test text for biography')


    def test_create_post(self):
        """CREATE POST in DATABASE"""
        self.post = Post.objects.create(title='TestPost1', text='test text test text', category='1', author=self.profile,
                                        public_time=timezone.now(),
                                        img=get_img())
        self.post.save()
        pk = self.post.pk
        response = client.get('/post/' + str(pk))
        self.assertEqual(response.status_code, 200)


    def test_comment(self):
        """CREATE COMMENT in DATABASE"""
        self.post = Post.objects.create(title='TestPost1', text='test text test text', category='1', author=self.profile,
                                        public_time=timezone.now(),
                                        img=get_img())
        self.comment = Comment.objects.create(post=self.post, text='my first comment', created=timezone.now())
        pk = self.post.pk
        self.assertEqual(Comment.objects.first().text, 'my first comment')
        response = client.get('/post/' + str(pk))
        self.assertEqual(response.status_code, 200)



###################### VIEWS TESTING ####################################

class PostViewTest(TestCase):
    """Create post by form"""
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='2test@12346', password='12test12', email='test@example.com')
        self.user.save()
        self.profile = Profile.objects.create(login=self.user,
                                              name='Alisa', last_name='Ivanova',
                                              date_birth='2021-12-07',
                                              email='test@example.com',
                                              bio='Test text for biography')

        self.person = reverse('personal_page')

    def test_create_post(self):
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        response = client.post(self.person, {'title': 'TestPost2',
                                                  'text': 'text by testpost2',
                                                  'category': 1,
                                                  'img': get_img()
                                                  })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.first().title, 'TestPost2')
        self.assertTemplateUsed('user/personal_page.html')

    def test_delete_post(self):
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        self.post = Post.objects.create(title='TestPost1', text='test text test text', category='1', author=self.profile,
                                        public_time=timezone.now(),
                                        img=get_img())
        self.post.save()
        pk = self.post.pk
        self.delete_url = reverse('delete', args=[str(pk)])
        response = client.get('/api/profile/' + str(pk) +'/')
        self.assertEqual(response.status_code, 200)
        client.delete(self.delete_url, json.dumps({'pk': pk}))
        self.assertEqual(Post.objects.count(), 0)
        self.assertTemplateUsed('user/detail_post.html')

    def test_update_post(self):
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        self.post = Post.objects.create(title='TestPost2', text='test text test text', category='1',
                                        author=self.profile,
                                        public_time=timezone.now(),
                                        img=get_img())
        self.post.save()
        pk = self.post.pk
        self.update_url = reverse('update', args=[str(pk)])
        client.post(self.update_url, {'title': 'Change', 'text': 'test text test text', 'category': '1',
                                      'author': self.profile,
                                      'public_time': timezone.now(),
                                      'img': get_img()})
        self.assertEqual(Post.objects.first().title, 'Change')


class CreateCommentViewTest(TestCase):
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
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        pk = self.post.pk
        self.detail_post_url = reverse('post_detail', args=[str(pk)])
        response = client.get(self.detail_post_url)
        self.assertEqual(response.status_code, 200)
        client.post(self.detail_post_url, {'text': 'comment text'})
        self.assertEqual(Comment.objects.first().text, 'comment text')


class FollowingTestView(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='2test@12346', password='12test12', email='test@example.com')
        self.user.save()
        self.another_user = User.objects.create_user(username='test2', password='12test12', email='test@example.com')
        self.user.save()
        self.profile = Profile.objects.create(login=self.user,
                                              name='Alisa', last_name='Ivanova',
                                              date_birth='2021-12-07',
                                              email='test@example.com',
                                              bio='Test text for biography')

    def test_following(self):
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        self.profile.followers.add(self.another_user)
        profile = Profile.objects.get(login=self.user)
        self.assertEqual(profile.followers.count(), 1)
        self.profile.followers.remove(self.another_user)
        self.assertEqual(profile.followers.count(), 0)


class NewsTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='2test@12346', password='12test12', email='test@example.com')
        self.user.save()
        self.profile = Profile.objects.create(login=self.user,
                                              name='Alisa', last_name='Ivanova',
                                              date_birth='2021-12-07',
                                              email='test@example.com',
                                              bio='Test text for biography')
        #############################################################################################################
        self.another_user = User.objects.create_user(username='test2', password='12test12', email='test@example.com')
        self.user.save()
        self.profile2 = Profile.objects.create(login=self.another_user,
                                              name='Sasha', last_name='Dubova',
                                              date_birth='2021-12-07',
                                              email='test1@example.com',
                                              bio='Test text for biography')
        #############################################################################################################
        self.user3 = User.objects.create_user(username='test3', password='12test12', email='test@example.com')
        self.user.save()
        self.profile3 = Profile.objects.create(login=self.user3,
                                              name='Vova', last_name='Ivanov',
                                              date_birth='2021-12-07',
                                              email='tesft@example.com',
                                              bio='Testf text for biography')

        ##########################################
        self.post = Post.objects.create(title='TestPost11', text='test1 text 1test 1text1', category='1',
                                        author=self.profile,
                                        public_time=timezone.now(),
                                        )

        ###########################################
        self.post2 = Post.objects.create(title='TestPost222', text='tes2t text2 test2text2', category='1',
                                        author=self.profile2,
                                        public_time=timezone.now(),
                                        )
        ###################################################
        self.post3 = Post.objects.create(title='TestPost33', text='test3 text3 test 3text3', category='1',
                                        author=self.profile3,
                                        public_time=timezone.now(),
                                        )
        self.post4 = Post.objects.create(title='TestPost44', text='test3 text3 test 3text3', category='1',
                                         author=self.profile2,
                                         public_time=timezone.now(),
                                         )

    def test_news_list(self):
        """ test should skip the post of unfollow user"""
        client.post('/accounts/login/', {'username': '2test@12346', 'password': '12test12'}, follow=True)
        self.profile.followers.add(self.another_user)
        self.news_url = reverse('news')
        response = client.get(self.news_url)
        self.assertEqual(response.status_code, 200)
        post_user2 = response.context['posts'].object_list[1]
        self.assertEquals(post_user2.title, 'TestPost222')
        my_post = response.context['posts'].object_list[2]
        self.assertEquals(my_post.title, 'TestPost11')
        post_user3 = response.context['posts'].object_list[0]
        self.assertNotEqual(post_user3.title, 'TestPost33')
