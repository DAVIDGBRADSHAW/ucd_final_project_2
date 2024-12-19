from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView # New import added here
)

from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, 'home.html', {})


class HomeView(ListView,LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'home.html'
    fields = ['title', 'content','first_name', 'surnname', 'Email ', 'ADDRESS_1','ADDRESS_2', 'ADDRESS_3', 'ADDRESS_4','ADDRESS_5', 'CODE','WHY', 'date_posted',
    'MAILING_LIST','author',
]

class ArticleDetailView(DetailView):
    model = Post
    template_name='article_detail.html'


def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostlistView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] 

class PostDetailView(DetailView):
    model = Post  
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 
    'first_name = models.CharField(max_length=30)', 'surname = models.CharField(max_length=30)', 
    'Email = models.CharField(max_length=100)', 
    'ADDRESS_1 = models.CharField(max_length=30)',
    'ADDRESS_2 = models.CharField(max_length=30)',
    'ADDRESS_3 = models.CharField(max_length=30)',
    'ADDRESS_4 = models.CharField(max_length=30)',
    'ADDRESS_5 = models.CharField(max_length=30)',
    'CODE = models.CharField(max_length=100)',
    'WHY= models.TextField()',
    'title = models.CharField(max_length=100)',
    'date_posted = models.DateTimeField(default=timezone.now)',
    'MAILING_LIST = models.ForeignKey(User, on_delete=models.CASCADE)',
    'content = models.TextField()',
    'author = models.ForeignKey(User, on_delete=models.CASCADE)',
    'content = models.TextField()', 
]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # New class PostDeleteView created here
    model = Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/" # Here we are redirecting the user back to the homepage after deleting a Post successfully
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False