from django.urls import path

from .views import *

urlpatterns = [
    path('', MusicMain.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ShowCat.as_view(), name='cat'),
]