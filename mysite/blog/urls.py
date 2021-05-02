from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from .import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/', PostListView.as_view(), name='blog-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('ecom/', views.ecom, name='ecom-ecom'),
]
