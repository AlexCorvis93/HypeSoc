from django.shortcuts import render
from .models import Post, Comment, User, Profile
from django.shortcuts import render
from .forms import CreateAnonymusCommentForm
from django.views.generic import ListView
from django.core.paginator import Paginator



def detail_and_comments(request, pk):
    """COMMENTS"""
    post = Post.objects.get(pk=pk)
    name = User.objects.all().filter(username=request.user)
    total_comment = post.comments.all()
    profile = Profile.objects.all()
    comments = post.comments.all().order_by('-created')[:3]
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
                                                     'form_comment': form, "total_comment": total_comment})


class NewsList(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'post'
    template_name = 'anonymus/anonym_news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context["profile"] = Profile.objects.all()
        return context