from django.urls import path, include, admin
from django.contrib.auth import views as auth_views, user_views
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Added import here
from django.contrib import messages
from .forms import UserRegisterForm

urlpatterns = [
   # path('', PostListView.as_view(), name='blog-home'),
    #path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
    #path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Added in new url pattern
    #path('about/',views.about, name='blog-about'),
    #path('', views.home, name="home"),
    path("admin/", admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   
    path('',include('blog.urls')), 
]