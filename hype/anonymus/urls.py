from django.urls import path, include
from .views import NewsList, detail_and_comments

urlpatterns = [
   path('', NewsList.as_view(), name='a_news'),# news page
   path('post/<int:pk>', detail_and_comments, name='post')# post_page

]