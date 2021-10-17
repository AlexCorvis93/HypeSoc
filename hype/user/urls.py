from django.urls import path
from . import views
from rest_framework import routers
from .api import ProfileViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, 'profile')
router.register('', PostViewSet, 'post')


urlpatterns = router.urls



