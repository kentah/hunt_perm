from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView

from .models import Post, Category


class PostActionMixin:
    ''' Mixin to create confirmation'''
    fields = ['title', 'slug', 'body', 'category']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(PostActionMixin, self).form_valid(form)


class Feed(ListView):

    model = Post
    template_name = '../templates/blog/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created')

    def full(self, request, post_id):
        return(post_id)


class Index(ListView):

    model = Post
    template_name = '../templates/blog/side.html'

    def getPosts(self, request, *args, **kwargs):

        data = Post.objects.all()

        return render(request, template_name, {'side': data})


class CreatePostView(CreateView, LoginRequiredMixin, PostActionMixin):
    template_name = '../templates/blog/create.html'
    model = Post
    fields = ['title', 'slug', 'body', 'category']
    success_msg = 'Post created!'


class UpdatePostView(UpdateView, LoginRequiredMixin, PostActionMixin):
    template_name = '../templates/blog/update.html'
    model = Post
    fields = ['title', 'slug', 'body', 'category']
    success_msg = 'Post updated!'


class Detail(DetailView):
    '''
    def individualPost(self, request):
        recentPost = Post.objects.get(id_exact=1)
        p = f'{recentPost.title}:{recentPost.content}'
        return render()
    '''
    pass
