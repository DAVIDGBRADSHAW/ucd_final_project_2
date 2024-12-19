from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, UpdateView,MyModel
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
#from .models import Posts
# Create your views here.x
 #def home(request):
#return render(request, 'home.html', {})
from .models import Contact
from django.contrib.auth.models import User
from django.shortcuts import render, get_list_or_404

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

def get_queryset(self):
    user = get_list_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-data_posted')
 


class HomeView(ListView,LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'home.html'
    fields = ['title', 'content','first_name', 'surnname', 'Email ', 'ADDRESS_1','ADDRESS_2', 'ADDRESS_3', 'ADDRESS_4','ADDRESS_5', 'CODE','WHY', 'date_posted',
    'MAILING_LIST','date_posted','author','date_posted','author',
]

class ArticleDetailView(DetailView):
    model = Post
    template_name='article_detail.html'


def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    paginate_by = 5
 
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
      
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ParishPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'first_name', 'surname', 'email', 'address_1', 'address_2', 'address_3', 'address_4', 'address_5', 'code',]
 
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

#class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
 #   model = Post
  #  success_url = '/' # Here we are redirecting the user back to the homepage after deleting a Post successfully
    
   # def test_func(self):
    #    post = self.get_object()
     #   if self.request.user == post.author:
      #      return True
       # return False
    


# 41min oct 3rd 2024

from django.views.generic.edit import DetailView, ListView
class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'myapp/my_model_detail.html'

class MyModelListView(ListView):
    model = MyModel
    template_name = 'myapp/my_model_list.html'

class FilteredMyModelListView(ListView):
     model = MyModel
    template_name = 'myapp/filted_model_list.html'

    def get_queryset(self):
        return

MyModel.objects.filter(attribute='some_value').order_by('-created_date')