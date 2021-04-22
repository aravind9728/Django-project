from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'blog/home.html',{"title" :'Home Page '})

def about(request):
    return render(request,'blog/about.html',{"title" :'About Page'})
    

