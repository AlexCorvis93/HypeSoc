from .models import Profile, Post
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer, PostSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """API for Profiles"""
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    """API for Post"""
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer