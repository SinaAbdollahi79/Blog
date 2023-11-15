from django.contrib import admin
from website.models import contact  

# Register your models here.
 
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("name", "subject", "email", "created_date", "updated_date")
    list_filter = ("name", "subject")
    search_fields = ("name","subject", "email","massage")

admin.site.register(contact, ContactAdmin)





    
