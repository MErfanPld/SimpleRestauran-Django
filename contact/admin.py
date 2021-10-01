from django.contrib import admin
from .models import Contact

# Register your models here.

#=====================ContactAdmin=====================

class ContactAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email",)
    list_filter = ("fullname",)
    search_fields = ("fullname", "email", "massage")
    ordering = ("fullname", "email",)

admin.site.register(Contact,ContactAdmin),