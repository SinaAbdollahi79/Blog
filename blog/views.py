from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import post, comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import commentform
from django.contrib import messages


# set filter for category and set pageinator
def blog(request, **kwargs):
    posts = post.objects.filter(status=1)
    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username"):
        posts = posts.filter(author__username=kwargs["author_username"])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get.page(1)
    except EmptyPage:
        posts = posts.get.page(1)

    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def single(request, pid):
    if request.method == "POST":
        form = commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ".تیکت شما با موفقیعت ثبت شد")
        else:
            messages.error(request, ".متاسفانه تیکت شما ثبت نشد")

    posts = post.objects.filter(status=1)
    posts = get_object_or_404(post, pk=pid)
    comments = comment.objects.filter(post=posts.id, approved=1).order_by(
        "-create_date"
    )
    froms = commentform()
    context = {"posts": posts, "comments": comments, "froms": froms}
    return render(request, "blog/blog-single.html", context)


def search(request):
    posts = post.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)

    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)
