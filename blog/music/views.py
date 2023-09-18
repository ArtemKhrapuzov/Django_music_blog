from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


class MusicMain(ListView):
    """Вывод всех постов"""
    model = Singer
    template_name = 'music/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Singer.objects.filter(is_published=True).select_related('cat')


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
    paginate_by = 3

    def get_queryset(self):
        return Singer.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class RegisterUser(CreateView):
    """Форма авторизации"""
    form_class = RegisterUserForm
    template_name = 'music/auth.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    """Форма входа"""
    form_class = LoginUserForm
    template_name = 'music/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    """Выход"""
    logout(request)
    return redirect('login')
