from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer
from rest_framework.response import Response


class ShowProfile(APIView):
        renderer_classes = [TemplateHTMLRenderer]
        serializer_class = ProfileSerializer
        template_name = 'user/profile.html'

        def get(self, request):
            queryset = Profile.objects.all()
            return Response({'profiles': queryset})


class ShowPost(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/posts.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'Posts': queryset})

