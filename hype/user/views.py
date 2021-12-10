from django.http import HttpResponse, Http404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Post, Comment
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreateCommentForm
from django.views.generic import ListView, DetailView
from .serializers import PostSerializer
from django.core.paginator import Paginator
from itertools import chain


def post_detail(request, pk):
    """COMMENTS"""
    post = get_object_or_404(Post, pk=pk)
    author = Profile.objects.get(login=request.user)
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

    return render(request, 'user/post_detail.html', {'post': post, 'comments': comments,
                                                     'form_comments': form, "total_comment": total_comment,
                                                     "author": author,
                                                     })



def delete(request, pk):
    """DELETE POST"""
    try:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect("/")
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
    return render(request, "user/version.html", {"object": profile, "post": post, "person": person})


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
    paginator = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user/news.html', {'posts': page_obj, 'prof': profile, 'profile_list': pr_list})





class New_post(APIView):
    """FORM POST CREATE API"""
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/create_post_api.html"
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        profile = Profile.objects.get(login=self.request.user)
        serializer.save(author=profile.name)

    def get(self, request):
          serializer = PostSerializer()
          return Response({'serializer': serializer})

    def post(self, request):
        profile = Profile.objects.get(login=self.request.user)
        serializer = PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer})
        post = serializer.save(author=profile)
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
    return render(request, 'user/comment_list.html', {"comments": comments})



def users_post_list(request):
    profile = Profile.objects.get(login=request.user)
    post = Post.objects.all().filter(author=profile)
    return render(request, "user/user_post_list.html", {"post": post})










































