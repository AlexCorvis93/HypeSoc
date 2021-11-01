from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated

from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer
from rest_framework.response import Response



class ShowProfile(APIView):
        permission_classes = [IsAuthenticated]
        queryset = Profile.objects.all()
        renderer_classes = [TemplateHTMLRenderer]
        serializer_class = ProfileSerializer
        template_name = 'user/profile.html'

        def get(self, request):
            queryset = Profile.objects.all().filter(login=request.user)

            return Response({'profiles': queryset})


class ShowPost(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/posts.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'Posts': queryset})

class ShowPersonPost(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/profile.html'

    def get(self, request):
        queryset = Post.objects.all().filter(autor=request.user)
        return Response({'Posts': queryset})
