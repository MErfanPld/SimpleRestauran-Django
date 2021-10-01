from django.contrib import admin
from .models import Stuffs

# Register your models here.

#=====================StuffAdmin=====================

class StuffAdmin(admin.ModelAdmin):
    list_display = ("fullname", "offer",)
    list_filter = ("offer",)
    search_fields = ("fullname", "offer", "face_book", "gmail", "instagram")
    ordering = ("fullname", "offer", "face_book", "gmail", "instagram")

admin.site.register(Stuffs,StuffAdmin),