from django.http import HttpResponse, Http404
from .models import Profile, Post, Comment
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateCommentForm, PostForm
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator
from itertools import chain
from PIL import Image

def post_detail(request, pk):
    """COMMENTS"""
    post = get_object_or_404(Post, pk=pk)
    author = Profile.objects.get(login=request.user)
    person = Profile.objects.all()
    total_comment = post.comments.all()
    comments = post.comments.filter(active=True).order_by('-created')[:3]
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()
    else:
        form = CreateCommentForm()

    return render(request, 'user/detail_post.html', {'post': post, 'comments': comments,
                                                     'form_comments': form, "total_comment": total_comment,
                                                     "author": author, 'person': person})



def PostCreate(request):
    profile = Profile.objects.get(login=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = profile
            new_post.save()
        else:
            form = PostForm()
    return render(request, "user/personal_page.html", {'form': form})



def PostApdate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.get(login=request.user)
    if request.method == 'GET':
        form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = profile
            new_post.save()
        else:
            form = PostForm()
    return render(request, "user/apdate_post.html", {'form': form, 'person': profile})



def delete(request, pk):
    """DELETE POST"""
    try:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect("news")
    except Post.DoesNotExist:
        return Response("<h2>Post not found</h2>")


def following(request):
    """FOLLOWING FUNCTION"""
    if request.method == 'POST':
        my_profile = Profile.objects.get(login=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.login in my_profile.followers.all():
            my_profile.followers.remove(obj.login)
        else:
            my_profile.followers.add(obj.login)
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect('main')


class ProfilePage(DetailView):
    """SHOW DETAIL USERS PAGE"""
    model = Profile
    template_name = 'user/another_profile.html'

    def get_context_data(self, *, object_list=None, **kwargs, ):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        view_profile = self.get_object()
        context['person'] = Profile.objects.all()
        context['post'] = Post.objects.all().filter(author=view_profile)
        my_profile = Profile.objects.get(login=self.request.user)
        if view_profile.login in my_profile.followers.all():
            follow = True
        else:
            follow = False
        context['follow'] = follow
        return context


def personalPage(request):
    """PERSONAL PAGE"""
    profile = Profile.objects.get(login=request.user)
    person = Profile.objects.all()
    post = Post.objects.all().filter(author=profile).order_by('-public_time')[:3]
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = profile
            new_post.save()
    else:
        form = PostForm()
    return render(request, "user/personal_page.html", {"object": profile, "post": post, "person": person, 'form': form})


def post_news(request):
    """NEWS LIST for FOLLOWING USER"""
    profile = Profile.objects.get(login=request.user)
    user_list = [login for login in profile.followers.all()]
    pr_list = Profile.objects.all()
    posts = []
    for user in user_list:
        profile_get = Profile.objects.get(login=user)
        p = Post.objects.all().filter(author=profile_get)
        posts.append(p)
    my_post = Post.objects.all().filter(author=profile)
    posts.append(my_post)
    if len(posts) > 0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.title)
    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user/news2.html', {'posts': page_obj, 'prof': profile, 'profile_list': pr_list})




class PeopleList(ListView):
    """USERS LIST for search people"""
    model = Profile
    paginate_by = 10
    template_name = 'user/people_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PeopleList, self).get_context_data(**kwargs)
        context["person"] = Profile.objects.all().exclude(login=self.request.user)
        return context





def CommentList(request, pk):
    """SHOW ALL COMMENTS"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().filter(active=True)
    person = Profile.objects.all()
    return render(request, 'user/comment_list.html', {"comments": comments, 'person': person})



def users_post_list(request):
    profile = Profile.objects.get(login=request.user)
    post = Post.objects.all().filter(author=profile)
    return render(request, "user/user_post_list.html", {"post": post})










































