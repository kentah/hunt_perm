from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import View, TemplateView, ListView

from .models import Post, Category


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

        return rendere(request, template_name, {'side': data})
