from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name="create"),
    path('feed/', views.feed, name='feed'),
    path('like/', views.liked_post, name='liked_post')
]
