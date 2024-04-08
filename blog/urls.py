from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = "blog"

urlpatterns = [
    path("", blog, name="blog"),
    path("<int:pid>", single, name="blog-single"),
    path("category\<str:cat_name>", blog, name="category"),
    path("author\<str:author_username>", blog, name="author"),
    path("search\ ", search, name="search"),
    path("rss/feed/", LatestEntriesFeed()),
]
