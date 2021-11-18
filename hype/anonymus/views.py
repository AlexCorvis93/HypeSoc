from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Profile, Post, AnonymusComment, User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateAnonymusCommentForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator



def detail_and_comments(request, pk):
    """COMMENTS"""
    post = Post.objects.get(pk=pk)
    name = User.objects.all().filter(username=request.user)
    total_comment = post.comment.all()
    comments = post.comment.all().order_by('-created')[:3]
    if request.method == 'POST' and request.user.is_anonymous:
        form = CreateAnonymusCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
    else:
        form = CreateAnonymusCommentForm()
    return render(request, 'anonymus/comments.html', {'comment': comments, 'post': post,
                                                     'form_comment': form, "total_comment": total_comment,
                                                     })


class NewsList(ListView):
    model = Post
    paginate_by = 4
    context_object_name = 'post'
    template_name = 'anonymus/anonym_news.html'