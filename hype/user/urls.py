from django.urls import path, include
from .views import *
from likes.views import LikeApi

urlpatterns = [
   path('personal_page/<int:pk>/', ProfilePage.as_view(), name='profile_page'),# another users page
   path('personal_page/', personalPage, name='personal_page'),# your profile page
   path("people/", PeopleList.as_view(), name='people'),# people list
   path('profile/<int:pk>/', post_detail, name='post_detail'),# post detail page
   path('delete/<int:pk>/', delete, name='delete'),# delete function
   path("followers/", following, name='following'),# following button
   path('', post_news, name='news'),#news by following users
   path('likes/<int:pk>/', LikeApi.as_view(), name='like'), #LIKES
   path('comments/<int:pk>/', CommentList, name="comments"),# COMMENTS_LIST
   path('userposts/', users_post_list, name='userposts'),
   path('update_post/<int:pk>/', PostUpdate, name='update'),#UPDATE POST

]









