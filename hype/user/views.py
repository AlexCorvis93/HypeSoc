from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Profile, Post
from .api import ProfileViewSet
from .serializers import ProfileSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ShowProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user/profile.html'

    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})




def post_list(request):
    """прозвонка шаблона с БД"""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'user/profile.html', context=context)









