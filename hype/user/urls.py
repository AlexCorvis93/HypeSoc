from django.urls import path, include
from .views import *

urlpatterns = [
   path('profile/', ShowProfile.as_view(), name='profile'),#personal page
   path('', ShowPosts.as_view(), name='main'),#main page
   path('profile/<int:pk>/', post_detail, name='post_detail'),# post detail page
   path('profile/new_post/', New_post.as_view(), name='create_post'),
   path('test/<int:pk>/', NewPostDetail.as_view(), name="new_posT"),
   path('delete/<int:pk>/', delete, name='delete'),


]









