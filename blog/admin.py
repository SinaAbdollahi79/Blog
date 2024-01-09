from django.contrib import admin
from blog.models import post,categories
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("titel","author", "status", "created_date", "published_date")
    list_filter = ("status", "created_date", "published_date")
    search_fields = ("titel","status", "created_date")
    summernote_fields = ('content')


admin.site.register(post, PostAdmin)
admin.site.register(categories)

