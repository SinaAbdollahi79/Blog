from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages
from django.conf import settings
from blog.models import post


def home(request):
    posts = post.objects.filter(status=1, first_page_published=1)
    context = {"posts": posts}
    return render(request, "website/index.html",context)


def about(request):
    return render(request, "website/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ".تیکت شما با موفقیعت ثبت شد")
        else:
            messages.error(request, ".متاسفانه تیکت شما ثبت نشد")
    form = ContactForm()

    return render(request, "website/contact.html", {"form": form})
