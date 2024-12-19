from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView, PostDeleteView,  ArticleDetailView,UserPostListView, HomeView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
     path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Added in new url pattern
    path('about/',views.about, name='blog-about'),
    path('', include('blog.urls')),
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('post/<int:pk/delete',PostDeleteView.as_view(), name='user-post-delete'),
    
]