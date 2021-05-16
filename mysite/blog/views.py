from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
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

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

