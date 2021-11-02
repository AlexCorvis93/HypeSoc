from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
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
            cont = Post.objects.all().filter(author=request.user)
            return Response({'profiles': queryset, 'post': cont})


class ShowPost(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/posts.html'


    def get(self, request):
        queryset = Post.objects.all()
        cont = Profile.objects.all()
        return Response({'Posts': queryset, 'prof': cont})



# class ShowPersonPost(APIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'user/profile.html'
#
#
#     def get(self, request):
#         queryset = Post.objects.all().filter(author=request.user)
#         return Response({'post': queryset})
