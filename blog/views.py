from django.shortcuts import render
from django.http import HttpResponse   

def blog(request):
    return render(request, 'Blog/blog-home.html')

def single(request):
    return render(request, 'Blog/blog-single.html')