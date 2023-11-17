from django.shortcuts import render
from django.http import HttpResponse   
from blog.models import post 

def blog(request):
    posts = post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'Blog/blog-home.html', context)

def single(request):
    return render(request, 'Blog/blog-single.html')