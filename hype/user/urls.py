from django.urls import path, include
from .views import *

urlpatterns = [
   path('personal_page/<int:pk>/', ProfilePage.as_view(), name='profile_page'),# another users page
   path('personal_page/', personalPage, name='personal_page'),
   path('', post_news, name='main'),#main page
   path('profile/<int:pk>/', post_detail, name='post_detail'),# post detail page
   path('profile/new_post/', New_post.as_view(), name='create_post'),
   path('test/<int:pk>/', NewPostDetail.as_view(), name="new_posT"),
   path('delete/<int:pk>/', delete, name='delete'),
   path("followers/", following, name='following'),






]









