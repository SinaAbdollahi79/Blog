from django.contrib import admin
from website.models import contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("name", "last_name", "subject", "email", "created_date")
    list_filter = ("name", "last_name", "subject")
    search_fields = ("name", "last_name", "subject", "email", "massage")


admin.site.register(contact, ContactAdmin)
