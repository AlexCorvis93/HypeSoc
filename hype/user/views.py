from django.http import HttpResponse, Http404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Post, Follower
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateCommentForm
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets, status
from .serializers import PostSerializer
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage

def post_detail(request, pk):
    """COMMENTS"""
    post = get_object_or_404(Post, pk=pk)
    total_comment = post.comments.all()
    comments = post.comments.filter(active=True).order_by('-created')[:3]
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CreateCommentForm()
    return render(request, 'user/post_detail.html', {'post': post, 'comments': comments,
                                                     'form_comments': form, "total_comment": total_comment})


def delete(request, pk):
    """DELETE POST"""
    try:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect("/")
    except Post.DoesNotExist:
        return Response("<h2>Post not found</h2>")



class ProfilePage(DetailView):
    """SHOW DETAIL USERS PAGE"""
    model = Profile

    def get_context_data(self, *, object_list=None, **kwargs, ):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all().filter(author=self.object.login)
        return context



def personalPage(request):
    """PERSONAL PAGE"""
    profile = Profile.objects.all().filter(login=request.user)
    post = Post.objects.all().filter(author=request.user.id)
    return render(request, "user/profile_page.html", {"object": profile, "post": post})


class ShowPosts(ListView):
    """SHOW POSTS in main page"""
    model = Post
    paginate_by = 3
    context_object_name = 'post'
    template_name = 'user/posts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowPosts, self).get_context_data(**kwargs)
        context['prof'] = Profile.objects.all()
        return context


class New_post(APIView):
    """FORM POST CREATE API"""
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/create_post_api.html"
    permission_classes = [IsAuthenticated]

    def get(self, request):
          serializer = PostSerializer()
          return Response({'serializer': serializer})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer})
        post = serializer.save()
        return redirect('new_posT', pk=post.pk)


class NewPostDetail(APIView):
    """GET UPDATE post REST_Framework"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/new_api_post.html"

    def get_object(self, pk):
        try:
            return get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response({'serializer': serializer, 'post': post})

    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, "post": post})
        serializer.save()
        return redirect('post_detail')
























































