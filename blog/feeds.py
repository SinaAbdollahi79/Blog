from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post


class LatestEntriesFeed(Feed):
    title = "new postes"
    link = "/rss/feed"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return post.objects.filter(status=True)

    def item_titel(self, item):
        return item.titel

    def item_content(self, item):
        return item.content[:100]
