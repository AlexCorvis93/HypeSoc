from django.urls import path, include
from .views import *

urlpatterns = [
   path('profile/', ShowProfile.as_view(), name='profile'),#personal page
   path('', ShowPosts.as_view(), name='main'),#main page
   path('profile/new_post/', post_new, name='new_post'),# create post page
   path('profile/<int:pk>/', post_detail, name='post_detail')# post detail page


]









