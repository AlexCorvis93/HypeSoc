
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Post
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateCommentForm, CreatePostForm
from django.views.generic import ListView


def post_detail(request, pk):
    """COMMENTS"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CreateCommentForm()
    return render(request, 'user/post_detail.html', {'post': post, 'comments': comments, 'form_comments': form})



def post_new(request):
    """CREATE POST"""
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CreatePostForm()
    return render(request, 'user/create_post.html', {'form': form})



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


class ShowProfile(APIView):
        """SHOW PERSONAL PAGE"""
        permission_classes = [IsAuthenticated]
        queryset = Profile.objects.all()
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'user/profile.html'

        def get(self, request):
            queryset = Profile.objects.all().filter(login=request.user)
            cont = Post.objects.all().filter(author=request.user)
            return Response({'profiles': queryset, 'post': cont})



















































































