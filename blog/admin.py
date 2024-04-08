from django.contrib import admin
from blog.models import post, categories, comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("titel", "author", "status","first_page_published", "created_date", "published_date")
    list_filter = ("status", "created_date", "published_date")
    search_fields = ("titel", "status", "created_date")


class commentsAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "approved", "post")
    list_filter = ("approved", "post")


admin.site.register(comment, commentsAdmin)
admin.site.register(post, PostAdmin)
admin.site.register(categories)
