from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
   path('profile/', ShowProfile.as_view(), name='profile'),#personal page
   path('', ShowPosts.as_view(), name='main'),#main page
   # path('profile/new_post/', post_new, name='new_post'),# create post page
   path('profile/<int:pk>/', post_detail, name='post_detail'),# post detail page
   path('profile/new_post/', New_post.as_view(), name='new_post'),
   path('test/<int:pk>/', NewPostDetail.as_view(), name="new_posT"),
]









