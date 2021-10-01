from django.contrib import admin
from .models import Sliders

# Register your models here.

#=====================SlidersAdmin=====================

class SlidersAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name", )

admin.site.register(Sliders,SlidersAdmin),