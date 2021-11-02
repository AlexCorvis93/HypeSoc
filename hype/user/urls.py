from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers


urlpatterns = [
    path('profile/', views.ShowProfile.as_view()),
    path('', views.ShowPost.as_view()),
    # path('profile_post/', views.ShowPersonPost.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)








