from django.contrib import admin
from blog.models import post,categories,comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("titel","author", "status", "created_date", "published_date")
    list_filter = ("status", "created_date", "published_date")
    search_fields = ("titel","status", "created_date")
    summernote_fields = ('content')

class commentsAdmin(admin.ModelAdmin):
    list_display = ("subject","name", "approved")
    list_filter = ("approved","post") 


admin.site.register(comment, commentsAdmin)
admin.site.register(post, PostAdmin)
admin.site.register(categories)

