from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    return render(request, 'blog/home.html',{'title': 'Home Page'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def ecom(request):
    return render(request, 'blog/ecom.html', {'title': 'E-commerce'})

def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']