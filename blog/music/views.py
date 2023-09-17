from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class MusicMain(ListView):
    model = Singer
    template_name = 'music/index.html'
    context_object_name = 'posts'


class ShowPost(DetailView):
    model = Singer
    template_name = 'music/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
