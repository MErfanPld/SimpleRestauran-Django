from django.contrib import admin
from .models import Foods

# Register your models here.

#=====================FoodAdmin=====================

class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "image_field", "price", "type_food")
    list_filter = ("type_food",)
    search_fields = ("name", "price", "type_food")
    ordering = ("name", "price", "type_food")

admin.site.register(Foods,FoodAdmin),