from django.shortcuts import render
from app_blog.models import *
from app_blog.forms import *

# VISTAS BASADAS EN CLASE

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# Create your views here.

def home(request):
    
    posts = Post.objects.all()

    return render(request, 'app_blog/home.html', {"title": "Home", "message": "Título del blog", "posts": posts})

class PostsList(ListView):

    model = Post
    template_name = "app_blog/post_list.html"

class PostDetail(DetailView):

    model = Post
    template_name = "app_blog/post_detail.html"

class PostCreate(CreateView):

    model = Post
    success_url = "/pages/"
    fields = ['title', 'subtitle', 'body', 'author', 'date', 'image']

class PostUpdate(UpdateView):

    model = Post
    success_url = "/pages/"
    fields = ['title', 'subtitle', 'body']

class PostDelete(DeleteView):

    model = Post
    success_url = "/pages/"

def about(request):
    
    return render(request, 'app_blog/about.html', {"title": "Acerca de este blog"})