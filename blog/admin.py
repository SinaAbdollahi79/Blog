from django.contrib import admin
from blog.models import post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("titel", "status", "created_date", "published_date")
    list_filter = ("status", "created_date", "published_date")
    #ordering = ["-created_date"]
    search_fields = ("titel","status", "created_date")


admin.site.register(post, PostAdmin)
