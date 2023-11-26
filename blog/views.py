from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import post


def blog(request):
    posts = post.objects.filter(status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def single(request, pid):
    posts = get_object_or_404(post, pk=pid, status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-single.html", context)
