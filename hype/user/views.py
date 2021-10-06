from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Profile, Post


def post_list(request):
    """прозвонка шаблона с БД"""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'user/profile.html', context=context)






