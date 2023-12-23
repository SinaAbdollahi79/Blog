from blog.models import categories, post
from django import template

register = template.Library()


@register.inclusion_tag("Blog/blog-postcatgories.html")
def printtags():
    postes = post.objects.filter(status=1)
    category = categories.objects.all()
    cat_dic = {}
    for name in category:
        cat_dic[name] = postes.filter(category=name).count()
    return {"category": cat_dic}


@register.simple_tag()
def postname():
    posts = post.objects.filter(status=1).order_by("published_date")[:2]

    return posts
