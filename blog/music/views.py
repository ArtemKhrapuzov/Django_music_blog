from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class MusicMain(ListView):
    """Вывод всех постов"""
    model = Singer
    template_name = 'music/index.html'
    context_object_name = 'posts'


class ShowPost(DetailView):
    """Вывод выбранного поста"""
    model = Singer
    template_name = 'music/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class ShowCat(ListView):
    """Вывод постов по категориям"""
    model = Singer
    template_name = 'music/index.html'
    slug_url_kwarg = 'cat_slug'
    context_object_name = 'posts'

    def get_queryset(self):
        return Singer.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')
