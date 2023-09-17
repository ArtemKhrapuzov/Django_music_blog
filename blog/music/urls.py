from django.urls import path

from .views import *

urlpatterns = [
    path('', MusicMain.as_view()),
    path('<slug:post_slug>/', ShowPost.as_view(), name='post')
]