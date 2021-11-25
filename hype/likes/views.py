from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Post, Profile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions


class LikeApi(APIView):
    """API for LIKES"""
    def get(self, request, pk):
        obj = get_object_or_404(Post, pk=pk)
        user = self.request.user
        updated = False
        liked = False
        if user in obj.likes.all():
            liked = False
            obj.likes.remove(user)
        else:
            liked = True
            obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
             "liked": liked,
        }
        return Response(data)







