from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class MusicMain(ListView):
    model = Singer
    template_name = 'music/index.html'
    context_object_name = 'posts'



